#!/usr/bin/python2.6
import db_connect
    
def create_tmp_bookprice(dB):    
    #To create the tmp_bookprice table:pass 1 
    sqlQuery1 = """SELECT
                bookmetadata_id,currency,max(effect_date) AS effect_date
                INTO TEMP tmp_price_dateonly
                FROM raw_bookprice
                GROUP BY bookmetadata_id,currency;
                """
                
    #To create the tmp_bookprice table:pass 2 
    sqlQuery2 = """SELECT
                bp.bookmetadata_id, bp.currency, bp.effect_date, bp.amount
                INTO TEMP tmp_bookprice
                FROM raw_bookprice bp, tmp_price_dateonly tp
                WHERE bp.bookmetadata_id = tp.bookmetadata_id AND bp.currency = tp.currency AND bp.effect_date = tp.effect_date;
                """
                
    #To create the tmp_bookprice_solo_entry table.  This tabulates all isbns with a single price entry             
    sqlQuery3 = """SELECT
                count(*), bookmetadata_id, currency,  amount
                INTO TEMP tmp_bookprice_solo_entry
                FROM tmp_bookprice tbp
                GROUP BY bookmetadata_id, currency, amount
                HAVING count(*) = 1
                ;
                """
    dB.ChangeQuery(sqlQuery1)
    #print sqlQuery2           
    dB.ChangeQuery(sqlQuery2)
    
    #print sqlQuery3           
    dB.ChangeQuery(sqlQuery3)
    
    
def update_tmp_details(dB):
    #Add 2 columns to the temporary table;
    sqlQuery1=""" ALTER TABLE tmp_reports_details ADD COLUMN list_price text, ADD COLUMN list_currency text ;"""
    
    #Updating the temporary table: match customer currency           
    sqlQuery2 = """UPDATE tmp_reports_details trd
                SET list_price = (SELECT tbp.amount FROM tmp_bookprice tbp WHERE tbp.bookmetadata_id =  trd.isbn AND tbp.currency = trd.customer_curr),
                    list_currency = (SELECT tbp.currency FROM tmp_bookprice tbp WHERE tbp.bookmetadata_id =  trd.isbn AND tbp.currency = trd.customer_curr)
                WHERE list_price IS NULL OR list_price ='';
                """
    #Updating the temporary table: customer currency did not match, so get the USD value            
    sqlQuery3 = """UPDATE tmp_reports_details trd
                SET list_price = (SELECT tbp.amount FROM tmp_bookprice tbp WHERE tbp.bookmetadata_id =  trd.isbn AND tbp.currency != trd.customer_curr AND tbp.currency = 'USD'),
                    list_currency = (SELECT tbp.currency FROM tmp_bookprice tbp WHERE tbp.bookmetadata_id =  trd.isbn  AND tbp.currency != trd.customer_curr AND tbp.currency = 'USD')
                 WHERE list_price IS NULL OR list_price ='';
                """
    #Updating the temporary table: last pass. If there is only one entry for the book prices, get that value.          
    sqlQuery4 = """UPDATE tmp_reports_details trd
                SET list_price = (SELECT tbps.amount FROM tmp_bookprice_solo_entry tbps WHERE tbps.bookmetadata_id =  trd.isbn),
                    list_currency = (SELECT tbps.currency FROM tmp_bookprice_solo_entry tbps WHERE tbps.bookmetadata_id =  trd.isbn)
                 WHERE list_price IS NULL OR list_price ='';"""
                 
    dB.ChangeQuery(sqlQuery1)
            
    dB.ChangeQuery(sqlQuery2)
              
    dB.ChangeQuery(sqlQuery3)
    
    dB.ChangeQuery(sqlQuery4)
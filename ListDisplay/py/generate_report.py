#!/usr/bin/python2.6
import db_connect
import commom_sql

import math, datetime


dB=db_connect.OpenDB()

#sql query1: create temporary table dl
common_sql.create_tmp_table(dB)




#close db connection
dB.Close()



#loop through results
for publisher_row in publisher_list_results:
        thisrow = etree.SubElement(table,"tr")
        thisrow.set("class", "alternator-gray")
      
        thiscode = etree.SubElement(thisrow,"td")
        thiscode.text = publisher_row[0]
  
        thisname = etree.SubElement(thisrow, "td")
        if publisher_row[1]:
            thisname.text = publisher_row[1]
        else:
            thisname.text = ""
  
        thisbookcut = etree.SubElement(thisrow,"td")
        thisbookcut.text = str(publisher_row[2])

        thiskidsbookcut = etree.SubElement(thisrow,"td")
        #thiskidsbookcut.text = str(publisher_row[3])
        thiskidsbookcut.text = str(publisher_row[3])
    
        thissmcut = etree.SubElement(thisrow,"td")
        #thissmcut.text = str(publisher_row[4])
        thissmcut.text = str(publisher_row[4])
    
        thisactive = etree.SubElement(thisrow,"td")
        if (str(publisher_row[5]) == 't'):
            thisactive.text = "True"
        else:
            thisactive.text = "False"
            
        thisactions = deepcopy(actions)
        thisedit = thisactions.find(".//a[@class='edit-btn']")
        thisedit.set("href","publisheredit.py?code"+ publisher_row[0])
        thisdelete = thisactions.find(".//a[@class='delete-btn']")
        thisdelete.set("href","publisherdelete.py?code="+ publisher_row[0])
        thisrow.append(thisactions)

print "Content-type: text/html\n\n"
print etree.tostring(HTMLtree)
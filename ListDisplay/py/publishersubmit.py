#!/usr/bin/python2.6

from lxml import etree
from lxml.builder import ElementMaker
import lxml
import cgi
import db_connect

import lxml.html
from lxml.html.builder import *

# Import the DB code
import sys,simpledb, psycopg2

import cgitb

def HREF(*args):
    return {"href":' '.join(args)}
    
cgitb.enable()

form = cgi.FieldStorage()
parser = etree.HTMLParser()

#take the values of the various fields and send it to db to update for that publisher
publisher_code = form["code"].value
publisher_name = form["name"].value
publisher_book_cut = form["publisher-cut"].value
publisher_kids_book_cut = form["publisher-kids-cut"].value
sm_cut = form["sm-cut"].value
publisher_active = form["publisher-active"].value
description = form["description"].value
code_original = form["code-original"].value
action = form["action"].value

dB=db_connect.OpenDB()
        
query = """
        """

if not publisher_book_cut or publisher_book_cut=='':
    publisher_book_cut='0.00'

if not publisher_kids_book_cut or publisher_kids_book_cut=='':
    publisher_kids_book_cut='0.00'

if not sm_cut or sm_cut=='':
    sm_cut='0.00'

if not description or description=='':
    description=publisher_name

# Try to make the database updates/inserts
try:
    #iceberg_book_cut, iceberg_kids_book_cut, description, sm_percentage, active
    if action == 'create_new':        
        query = """
        INSERT INTO shared_publisher
        (code, name, iceberg_book_cut, iceberg_kids_book_cut,  sm_percentage, active, description,) 
        VALUES('""" + publisher_code + "', '" + publisher_name + "', '"+publisher_book_cut + "', '"+publisher_kids_book_cut + "', '"+sm_cut + "', '"+publisher_active + "', '" + description + "')"
        #print query
        dB.InsertQuery(query)
        message = "A new publisher has been successfully added."
    else:
        # This is an update
        query = """
        UPDATE shared_publisher
        SET  code = '%s', name = '%s',  iceberg_book_cut = '%s',  iceberg_kids_book_cut = '%s', sm_percentage = '%s', active='%s', description = '%s'
        WHERE code = '%s'
        """ % ( publisher_code, publisher_name, publisher_book_cut, publisher_kids_book_cut, sm_cut, publisher_active, description , code_original)  
        dB.ChangeQuery(query)
        message = "Your update for publisher '%s' was successful." % (code_original)
except psycopg2.IntegrityError as detail:
    message = """Unable to complete update.  Please verify the Publisher Information. Click """
    status = "error"
else:
    dB.Commit()
    status = "success"
finally:
    dB.Close()


print "Content-type: text/html\n"
HTMLtree = etree.parse("../edit-status.html", parser)
body = HTMLtree.find("body")
display_div = HTMLtree.find(".//div[@id='" + status + "']")
display_div.text = str(message)
if status == "error":
    edit_link = etree.SubElement(display_div, "a")
    edit_link.text = "here"
    edit_link.set('href', 'javascript:document.forms[0].submit()')
    edit_link.tail = " to re-enter the publisher details."
    publisher_form = etree.SubElement(body, "form")
    publisher_form.set("id", "publisher-form")
    publisher_form.set("name", "publisher-form")
    publisher_form.set("method", "POST")
    publisher_form.set("action", "/cgi-bin/publisheredit.py")
    publisher_form.set("enctype", "multipart/form-data")
    
    publisher_code_input = etree.SubElement(publisher_form, "input")
    publisher_code_input.set('name', 'code')
    publisher_code_input.set('value', publisher_code)
    publisher_code_input.set('type', 'hidden')
    
    publisher_code_original_input = etree.SubElement(publisher_form, "input")
    publisher_code_original_input.set('name', 'code-original')
    publisher_code_original_input.set('value', code_original)
    publisher_code_original_input.set('type', 'hidden')    
    
    promo_name_input = etree.SubElement(publisher_form, "input")
    promo_name_input.set('name', 'name')
    promo_name_input.set('value', publisher_name)
    promo_name_input.set('type', 'hidden')
    
    publisher_cut_input = etree.SubElement(publisher_form, "input")
    publisher_cut_input.set('name', 'publisher-cut')
    publisher_cut_input.set('value', publisher_book_cut)
    publisher_cut_input.set('type', 'hidden')

    publisher_kids_cut_input = etree.SubElement(publisher_form, "input")
    publisher_kids_cut_input.set('name', 'publisher-kids-cut')
    publisher_kids_cut_input.set('value', publisher_kids_book_cut)
    publisher_kids_cut_input.set('type', 'hidden')
    
    sm_cut_input = etree.SubElement(publisher_form, "input")
    sm_cut_input.set('name', 'sm-cut')
    sm_cut_input.set('value', sm_cut)
    sm_cut_input.set('type', 'hidden')
        
    publisher_active_input = etree.SubElement(publisher_form, "input")
    publisher_active_input.set('name', 'publisher-active')
    publisher_active_input.set('value', publisher_active)
    publisher_active_input.set('type', 'hidden')

    description_input = etree.SubElement(publisher_form, "input")
    description_input.set('name', 'description')
    description_input.set('value', description)
    description_input.set('type', 'hidden')

    action_input = etree.SubElement(publisher_form, "input")
    action_input.set('name', 'action')
    action_input.set('value', action)
    action_input.set('type', 'hidden')

body.set("onload","javascript:displayMessage('"+ status +"');")
print etree.tostring(HTMLtree)
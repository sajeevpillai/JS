#!/usr/bin/python2.6
import db_connect

# For date formatting
import datetime

# For dev/testing purposes.
import cgi
import cgitb 
cgitb.enable()

# Import lxml/etree.
from lxml import etree
import lxml
import lxml.html
from lxml.html.builder import *

# Bring in the HTML template and get parameters from the URL.
parser = etree.HTMLParser()
HTMLtree = etree.parse("../publisher-add-edit.html", parser)
params = cgi.FieldStorage()

publisher_code = ""
publisher_name = ""
publisher_cut = ""
publisher_kids_cut = ""
sm_cut = ""
publisher_active = ""

# If publisher-id is in the form, it means we are back from the edit status page
if "action" in params:
    if action == "re_edit":
        publisher_code = params["code"].value
        publisher_name = params["name"].value
        publisher_book_cut = params["publisher-cut"].value
        publisher_kids_book_cut = params["publisher-kids-cut"].value
        sm_cut = params["sm-cut"].value
        publisher_active = params["publisher-active"].value
    elif action == "create_new":
        pass
else:
    action="edit"
    # No action specified, and the default action is edit
    if "code" in params:
        publisher_code = params.getvalue("code")
        dB=db_connect.OpenDB()
        
        query = """
        select  p.code, p.name, p.iceberg_book_cut, p.iceberg_kids_book_cut, p.sm_percentage, p.active
        from shared_publisher p
        where p.code = %s """ % (publisher_code)
        
        results = dB.SelectQuery(query)
        dB.Close()

        if results:
            #results are returned in a list.  grab the values from the first row.
            publisher_code = results[0][0]
            publisher_name = results[0][1]
            publisher_book_cut = results[0][2]
            publisher_kids_book_cut = results[0][3]
            sm_cut = results[0][4]
            publisher_active = results[0][5]

############# Hidden Fields
publisher_form = HTMLtree.find(".//form")
action_hidden = etree.SubElement(publisher_form, "input")
action_hidden.set("name","action")
action_hidden.set("value",action)
action_hidden.set("type","hidden")
code_orig_hidden = etree.SubElement(publisher_form, "input")
code_orig_hidden.set("name","code-original")
code_orig_hidden.set("value",code)
code_orig_hidden.set("type","hidden")

############# Code: value publisher_code
code_div = HTMLtree.findall(".//div[@id='code-div']")
code_field_right = etree.Element("div")
code_field_right.set("class", "field-right")
code_input = etree.SubElement(code_field_right, "input")
code_input.set("type", "text")
code_input.set("class", "")
code_input.set("name", "code")
code_input.set("value", publisher_code)
code_div[0].append(code_field_right)

############# Name: value publisher_name
name_div = HTMLtree.findall(".//div[@id='name-div']")
name_field_right = etree.Element("div")
name_field_right.set("class", "field-right")
name_input = etree.SubElement(name_field_right, "input")
name_input.set("type", "text")
name_input.set("class", "")
name_input.set("name", "name")
name_input.set("value", publisher_name)
name_div[0].append(name_field_right)

############# Publisher Share: value publisher_cut
cut_div = HTMLtree.findall(".//div[@id='cut-div']")
cut_field_right = etree.Element("div")
cut_field_right.set("class", "field-right")
cut_input = etree.SubElement(cut_field_right, "input")
cut_input.set("type", "text")
cut_input.set("class", "")
cut_input.set("name", "publisher-cut")
cut_input.set("value", publisher_cut)
cut_div[0].append(cut_field_right)  

############# Publisher Kids Share: value publisher_kids_cut
kids_cut_div = HTMLtree.findall(".//div[@id='kids-cut-div']")
kids_cut_field_right = etree.Element("div")
kids_cut_field_right.set("class", "field-right")
kids_cut_input = etree.SubElement(kids_cut_field_right, "input")
kids_cut_input.set("type", "text")
kids_cut_input.set("class", "")
kids_cut_input.set("name", "publisher-kids-cut")
kids_cut_input.set("value", publisher_kids_cut)
kids_cut_div[0].append(kids_cut_field_right)  
        
############# SM Share: value sm_cut
sm_div = HTMLtree.findall(".//div[@id='sm-cut-div']")
sm_field_right = etree.Element("div")
sm_field_right.set("class", "field-right")
sm_input = etree.SubElement(sm_field_right, "input")
sm_input.set("type", "text")
sm_input.set("class", "")
sm_input.set("name", "sm-cut")
sm_input.set("value", sm_cut)
sm_div[0].append(sm_field_right) 

############# SM Share: value publisher_active
active_div = HTMLtree.findall(".//div[@id='active-div']")
active_field_right = etree.Element("div")
active_field_right.set("class","field-right")
# Create the active dropdown.
active_select = etree.SubElement(region_field_right,"select")
active_select.set("name","publisher-active")
yesoption = etree.SubElement(active_select,"option")
yesoption.append("Yes", create_parent=True)
yesoption.set("value","t" )
if publisher_active == 't':
    yesoption.set("selected", "'selected'")
nooption = etree.SubElement(active_select,"option")
nooption.append("No", create_parent=True)
nooption.set("value", "f")
if publisher_active == 'f':
    thisoption.set("selected", "'selected'")    
active_div[0].append(active_field_right)

print "Content-type: text/html\n\n"
print etree.tostring(HTMLtree)

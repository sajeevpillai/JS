#!/usr/bin/python2.6

# For dev/testing purposes.
import cgi
import cgitb 
cgitb.enable()

import db_connect

# Import lxml/etree.
from lxml import etree
import lxml

import math, datetime
from copy import deepcopy

# Bring in the HTML template and get parameters from the URL.
parser = etree.HTMLParser()
HTMLtree = etree.parse("/publisher-list.html", parser)
params = cgi.FieldStorage()
PAGE = params.getvalue("page")
DISPLAY = params.getvalue("display")

if not PAGE:
    PAGE = '1'
    
if not DISPLAY:
    DISPLAY = '10'

OFFSET = (int(PAGE) - 1) * int(DISPLAY)

dB=db_connect.OpenDB()

if "delete" in params and "code" in params:
    PUBLISHER_CODE = params.getvalue("code")
    if params.getvalue("delete") == "true":        
        # delete the db entry for this publisher code
        query = """
        delete from shared_publisher
        where code = '%s' """ % (PUBLISHER_CODE)
        dB.ChangeQuery(query)        
        dB.Commit()

#get the count of promos for paging purposes
if "total-items" in params:
    totalitems = params["total-items"].value

#if totalitems is not set, retrieve number of publishers from database
if not 'totalitems' in locals():
    query = "select count(*) from shared_publisher"
    result_totalitems = dB.SelectQuery(query)
    totalitems = result_totalitems[0][0]
    #populate hidden field with totalitems
    publisher_list_form = HTMLtree.find(".//form")
    total = etree.SubElement(publisher_list_form, "input")
    total.set("name","totalitems")
    total.set("value",str(totalitems))
    total.set("type","hidden")

# Build pagination sections.
num_pages = int(math.ceil(float(totalitems)/float(DISPLAY)))

item_count = HTMLtree.findall(".//div[@id='total-items']")
item_count[0].text = str(totalitems)+" Total publishers"

page_lists = HTMLtree.findall(".//span[@class='page-list']")
spacer = " "
page_navtext = ""
page_navtail = ""

for x in range(1, num_pages+1):
  if x < int(PAGE):
    page_navtext = spacer.join((page_navtext, str(x)))
  elif x > int(PAGE):
    page_navtail = spacer.join((page_navtail, str(x)))

for child in page_lists:
  child.text = page_navtext+" "
  black = etree.SubElement(child, "span")
  black.text = PAGE
  black.set("class","blk")
  child.tail = page_navtail

prevbtn = HTMLtree.findall(".//a[@class='btn-prev-page']")
nextbtn = HTMLtree.findall(".//a[@class='btn-next-page']")

if 1 < int(PAGE) < num_pages:
  for btn in prevbtn:
    btn.set("href","publisherlist.py?display="+DISPLAY+"&page="+str(int(PAGE) - 1))
  for btn in nextbtn:
    btn.set("href","publisherlist.py?display="+DISPLAY+"&page="+str(int(PAGE) + 1))
elif int(PAGE) == 1:
  for btn in nextbtn:
    btn.set("href","publisherlist.py?display="+DISPLAY+"&page="+str(int(PAGE) + 1))
elif int(PAGE) == num_pages:
  for btn in prevbtn:
    btn.set("href","publisherlist.py?display="+DISPLAY+"&page="+str(int(PAGE) - 1))

#retrieve the list of publishers.
query = """
select  p.code, p.name, p.iceberg_book_cut, p.iceberg_kids_book_cut, p.sm_percentage, p.active
from shared_publisher p
order by p.active DESC, p.code limit %d offset %d """ % (int(DISPLAY), OFFSET)
publisher_list_results = dB.SelectQuery(query)

#close db connection
dB.Close()

#create the display list
browse_lists = HTMLtree.findall(".//table[@id='browselist']")
table = browse_lists[0]

actions = etree.Element("td")
miniholder = etree.SubElement(actions,"div")
miniholder.set("class","miniholder")
edit_link = etree.SubElement(miniholder,"a")
edit_link.set("class","edit-btn")
edit_action = etree.SubElement(edit_link,"div")
edit_action.set("class","customminibutton")
edit_action.text = "Edit"

del_link = etree.SubElement(miniholder,"a")
del_link.set("class","delete-btn")
del_action = etree.SubElement(del_link,"div")
del_action.set("class","customminibutton no-margin")
del_action.text = "Delete"

if not publisher_list_results:
    table.set("class","no-display")
    paging_list = HTMLtree.findall(".//div[@class='paging']")
    paging_list[0].set("class","no-display")
    paging_list_bot = HTMLtree.findall(".//div[@class='paging paging-bottom']") 
    paging_list_bot[0].set("class","no-display")
else:
    #p.code, p.name, p.iceberg_book_cut, p.iceberg_kids_book_cut, p.sm_percentage, p.active
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
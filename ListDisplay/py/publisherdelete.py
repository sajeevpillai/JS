#!/usr/bin/python2.6

from lxml import etree
from lxml.builder import ElementMaker
import lxml
import cgi

import cgitb
cgitb.enable()

params = cgi.FieldStorage()

if "code" in params:
    publisher_code = params.getvalue("code")

if "name" in params:
    publisher_name = params.getvalue("name")

parser = etree.HTMLParser()

#get confirmation
print "Content-type: text/html\n"
HTMLtree = etree.parse("../publisher-delete-confirm.html", parser)
confirm_message = HTMLtree.find(".//h3[@id='confirm-message']")
confirm_message.text = "Are you sure you would like to delete publisher " + publisher_name
confirm_button = HTMLtree.find(".//a[@id='confirm-button']")
confirm_button_link = "publisherlist.py?delete=true&code=" + publisher_code
confirm_button.set("href", confirm_button_link)
print etree.tostring(HTMLtree)

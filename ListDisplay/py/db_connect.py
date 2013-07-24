#!/usr/bin/python2.6

# Import the DB code
import sys,simpledb
#----------------- Open database
def OpenDB():
    #DatabaseType,Host,User,Password, Database
    #OpenedDB=simpledb.SimpledbClass("pgsql", "10.176.99.241", "dev", "smDEV", "dev");
    OpenedDB=simpledb.SimpledbClass("pgsql", "localhost", "django", "", "product_server");
    return OpenedDB

#----------------- Main

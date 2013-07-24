#!/usr/local/bin/python
#SimpleDB
#Python library by Francisco Reyes to do simple database operations easier
#Copyright Natserv Inc 2007 - 2011
#Francisco Reyes/Natserv grants Scrollmotion Inc a perpetual non exclusive right to use
#  this library
import sys
#
#
#

class SimpledbClass:
	"Simple Database Library"

	def __init__(self, DatabaseType,Host,User,Password, Database):
		self.Database_type = DatabaseType
		if (self.Database_type <> "mysql") and (self.Database_type <> "pgsql"):
			print "Database must be one of: mysql, pgsql"
			sys.exit

		if self.Database_type == "mysql":
			try:
				import MySQLdb
			except:
				print "Could not import MySQLdb"
				sys.exit()

			try:
				self.DB_Handle = MySQLdb.connect (host = Host, user = User, passwd = Password, db = Database)
				self.DB_cursor = self.DB_Handle.cursor()
			except:
				print "Mysql Conection to host " + Host + " failed"
				sys.exit()


		if self.Database_type == "pgsql":
			try:
				import psycopg2
			except:
				print "Could not import psycopg2"
				sys.exit()

			try:
				ConnectionString = "dbname='" +Database + "' user='" + User + "' host='"+ Host + "' password='"+Password +"'"
				self.DB_Handle = psycopg2.connect(ConnectionString)
				self.DB_cursor = self.DB_Handle.cursor()
			except:
				print "Postgresql Conection to host " + Host + " failed"
				sys.exit()

	def SelectQuery(self, Query_String):
		self.DB_cursor.execute(Query_String)
		return self.DB_cursor.fetchall()

	def ChangeQuery(self, Query_String):
		self.DB_cursor.execute(Query_String)

	def Close(self):
		self.DB_Handle.close()

	def Commit(self):
		self.DB_Handle.commit()

	def RollBack(self):
		self.DB_Handle.rollback()

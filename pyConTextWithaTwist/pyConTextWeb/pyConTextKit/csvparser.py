import csv
import array
import hashlib
import sqlite3
import os

class csvParser:
	"""
		Initializes the csvParser object with a csv file
		@param file String containing the path to the file
	"""
	def __init__(self,file):
		self.execute = True
		try:
			fileBIN = open(file,'rb')
		except IOError:
			print "File does not exist!"
		else:
			self.csvReader = sorted(csv.DictReader(open(file,'rb')))
	
	"""
		Prints md5 hexdigest of csvReader rows
		@precondition csvParser object must be instantiated first
	"""
	def rowHash(self):
		try:
			self.csvReader
		except NameError:
			print "You need to instantiate the csvParser class with a valid file first!"
		else:	
			for row in self.csvReader:
				return hashlib.md5(str(sorted(row.keys()))).hexdigest()
		
	"""
		Matches table name to hash
	"""
	def matchTable(self):
		signatures = {
			'b293cd42dda42b69a6e7b0cbff288b39': 'pyConTextKit_creator',
			'f0926b37e96a015c05f560fc21daef44': 'pyConTextKit_supercategory',
			'59e29a74cc10d0a429aaaa5505377cb4': 'pyConTextKit_category', 		
			'0fcc05e97edc5a953fa85d4a2ebdd760': 'pyConTextKit_itemrule',
			'78dca56aa59521629732b498e152d856': 'pyConTextKit_collection',
			'6ae2f59d723ed0c5d8d83aeddd85032f': 'pyConTextKit_itemdatum',
			'6283941eb6481137e01a77aa16e5ee4e': 'pyConTextKit_itemdatumset',
			'd6971d52331b336bb0616c30d9dfe24a': 'pyConTextKit_reporttype',					
			'ba39dd7a8908db13ca13bed83ad0fbc0': 'pyConTextKit_report',
			'8c063fd4dddbb381af4851ab1ed8f3d3': 'pyConTextKit_alert',
			'c5bc83a2d88c827f8e6bb572101db1e3': 'pyConTextKit_result'
		}
		
		sig = signatures[self.rowHash()]
		if len(sig) > 0: 
			return sig
		else:
			raise Exception("Signature not found!")
	
	"""
		Create SQL statements for inserting the information
		@param row type:list Row that contains the data that needs to be inserted
		Possible issues:
			I took out id from the SQL statments becuase it's PRIMARY AI and might interfere
	"""
	def createSQLStmt(self,row):
		sqlconfigs = {
			'pyConTextKit_creator': ['id','user_id'],
			'pyConTextKit_supercategory': ['id','name_supercategory'],
			'pyConTextKit_category': ['id','name_category'],									
			'pyConTextKit_itemrule': ['id','rule'],
			'pyConTextKit_collection': ['id','name','creator_id'],
			'pyConTextKit_itemdatum': ['id','supercategory_id','category_id','literal','re','rule_id','creator_id'],
			'pyConTextKit_itemdatumset': ['id','setname','itemDatum_id'],
			'pyConTextKit_reporttype': ['id','name'],									
			'pyConTextKit_report': ['id','dataset_id','reportid','reportType_id','report'],
			'pyConTextKit_alert': ['id','reportid','category','alert','report'],
			'pyConTextKit_result': ['id','reportid','category','disease','uncertainty','historical','literal','matchedphrase']
		}
		tablename = self.matchTable()
		
		sqlStmt = "INSERT INTO "+tablename+" ("
		
		sortedList = sorted(sqlconfigs[tablename])
		sqlconfig_mini = sortedList.pop()
		for i in sortedList:
			sqlStmt += i+", "
		sqlStmt += sqlconfig_mini
		
		sqlStmt += ") VALUES ("
		
		row_mini = row.pop()
		for i in row:
			sqlStmt += "'"+i+"', "
		sqlStmt += "'"+row_mini+"'"	
		
		sqlStmt += ");"
		
		return sqlStmt
	
	"""
		Reads a csv file row by row and calls createSQLStmt method executing SQL to modify database.
		@pre csvParser must be instantiated before iterateRows can be called
	"""
	def iterateRows(self):
		if self.execute:
			user_home = os.getenv('HOME')
			pyConTextWebHome = os.path.join(user_home,'pyConTextWeb')
			connection = sqlite3.connect(os.path.join(pyConTextWebHome,'pyConTextWeb.db'))
			c = connection.cursor()
		for row in self.csvReader:
			keysSorted = sorted(row.keys())
			valuesSorted = []
			for i in keysSorted:
				valuesSorted.append(row[i])
				
			""" Instead of printing execute it across the sql database """
			if self.execute:
				c.execute(self.createSQLStmt(valuesSorted))
			else:
				print self.createSQLStmt(valuesSorted)
		if self.execute:
			connection.commit()
			c.close()
		
		# Take care of error handling for the output of true/false
		return True
		
	

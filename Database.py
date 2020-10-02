# -*- coding: utf-8 -*-
"""
@author: nitika
"""

from table import Table
import datetime

class Database():
    
    def __init__(self,dbName):
        self.dbName = dbName
        self.createAt = datetime.datetime.now()
        self.dbTables={}
       
    # Attributes Format [("user_name","String"),("address","String"),("phone","Number"),("Mobile","Number")]
    
    def createTable(self,tableName,attributes):
        #print(type(attributes))
        if tableName in self.dbTables:
            print("table  ",tableName," already exist")
        else:
            user_table = Table(tableName,attributes)
            self.dbTables[tableName] = user_table
            print(tableName,"Table Created")
        
        return self.dbTables[tableName]
    
    def dropTable(self,tableName):
        
        if tableName not in self.dbTables:
            print("Table ",tableName," does not exist")
        else:
            
            del self.dbTables[tableName]
            print("Table ",tableName," dropped")
            
    def getCreatedAt(self):
        return self.createAt
    
    def selectTable(self,tableName):
        if tableName not in self.dbTables:
            print("Table does not exist")
        else:
            return self.dbTables[tableName]

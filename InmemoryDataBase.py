# -*- coding: utf-8 -*-
"""
@author: nitika
"""

from Database import Database


class DatabaseManager():
    
    def __init__(self):
       self.dataBases = {}
    
    def createDatabase(self,dbName):
        #dbName = input("Please enter the DataBase Name : ")
        
        if dbName in self.dataBases:
            print("Database  already exist")
        else:
            dataBase = Database(dbName)
            self.dataBases[dbName] = dataBase
            print(dbName," DataBase Created")
        
        return self.dataBases[dbName]
    
    def dropDatabase(self,dbName):
        #dbName = input("Please enter the DataBase Name to drop")
        
        if dbName not in self.dataBases:
            print("Database does not exist")
        else:
            
            del self.dataBases[dbName]
            print("Database ",dbName," dropped")
            
    def getDatabase(self,dbName):
        if dbName not in self.dataBases:
            print(dbName,"  Database does not exist")
        else:
            print("database : ",dbName)
            return self.dataBases[dbName]
        

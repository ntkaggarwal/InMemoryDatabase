# -*- coding: utf-8 -*-
"""
@author: nitika
"""
from InmemoryDataBase import DatabaseManager
from Database import Database
from table import Table
from row import Row


app = DatabaseManager()


print("_______________________ CREATE DATABASE _____________________________________")
# Question 4
print()
db1 = app.createDatabase("Verizon")

print()
verizonDB = app.getDatabase("Verizon")
print()

#table1 = db1.createTable("Employee",[("user_name","String"),("address","String"),("phone","Number")])
print("_______________________ CREATE TABLE _____________________________________")

print()

print()
emp = verizonDB.createTable("Employee",[("user_name","String"),("address","String"),("phone","Number")])
print()

print("_______________________ INSERT ROWS _____________________________________")

print()

print()
emp.insert([("user_name","Mayank Aggarwal"),("address","San Jose"),("phone",4568974452)])

#print(emp.get_rows())

emp.insert([("user_name","Nitika Aggarwal"),("address","Santa Clara"),("phone",1268974452)])

emp.insert([("user_name","Savita Aggarwal"),("address","Santa Clara"),("phone",1756974452)])

emp.insert([("user_name","Abc"),("address","33rd South"),("phone",32323212365)])
emp.insert([("user_name","Mayank"),("address","101 San"),("phone",4568974452)])
emp.insert([("user_name","Mayank"),("address","101 San"),("phone",3232321236)])
emp.insert([("user_name","Vijay"),("address","Golden Gate"),("phone",3232322589)])

print(emp.get_rows())
print()
print("_______________________ GET SPECIFIC ROWS _____________________________________")
print()

print(emp.get_rows(2))


print()
print("_______________________ GET ALL ROWS _____________________________________")
print()

print(emp.get_rows())

print()


print("_______________________DELETE_____________________________________")
# Question 4
emp.delete(2)

print("_______________________UPDATE__________________________________")

# Question 5
emp.update(1,{"user_name":"Swapnil","address":"33rd South","phone":232232})    
print(emp.get_rows())
print()


print("______________________SORTBYCOL______________________________________")

# Question 8
print()
print("SORTBY user_name"," asc")
print(emp.order_by("user_name","asc"))
print()

#print(emp.get_rows())


print("_______________________GROUPBYCOL_____________________________________")

# Question 9
print()
print(emp.group_by("address"))




print("_______________________ CREATE TABLE _____________________________________")

orderTable = verizonDB.createTable("Order", [("order_name","String"),("price","String"),("PIN","Number")])

print()
print("_______________________ INSERT ROWS _____________________________________")

orderTable.insert([("order_name","Grocery"),("price","1000"),("PIN",95112)])
orderTable.insert([("order_name","Electronics"),("price","2000"),("PIN",98112)])
print(orderTable.get_rows())
print()
print("_______________________ GET ALL ROWS _____________________________________")
print()
#print(emp.get_rows())
print(orderTable.get_rows())


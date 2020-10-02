# -*- coding: utf-8 -*-
"""
@author: nitika
"""
import datetime
from row import Row

class Table:
  table_name = ""

  def __init__(self,table_name, columns):
    self.table_name = table_name
    self.created_at = datetime.datetime.now()
    print(columns)
    self.columns = {name:value for name,value in columns}
    self.rows = {}
    self.row_id = 1

  # Question 3
  # Time complexity : O(len(columns))
  # Space complexity: O(len(columns))
  def insert(self, columns):
    if len(columns) == 0:
      print("Please give values for attributes")
      return 

    # only used by the insert function that's made it nested
    def get_column_dict(columns):
      column_dict = {}

      for name, value in columns:
        self.does_column_exists(name)
        column_dict[name] = value
      
      return column_dict

    try:
      row = Row(self.row_id, get_column_dict(columns))
      self.rows[self.row_id] = row
      self.row_id += 1
      # print("Row inserted")
    except BaseException as err:
      print(err)
  

  # Question 4
  # Time complexity : O(1)
  def delete(self, row_id):
    if row_id not in self.rows:
      print("Row not present")
    else:
      print("Deleting row",self.rows[row_id].get_attributes())
      del self.rows[row_id]
      print("Row deleted")


  # Question 5
  # Time complexity : O(len(columns))
  # Space complexity: O(len(columns))
  def update(self,row_id, columns):
    try:
      if row_id not in self.rows:
        raise Exception("Row not present")
      else:

        row_attributes = self.rows[row_id].get_attributes()

        # checking whether the column name is present in the table
        for column in columns:
          if column == "id" and row_attributes["id"] != columns[column]:
            raise Exception("Primary key cannot be updated")
            
          self.does_column_exists(column)

        for column in columns:
          row_attributes[column] = columns[column]
        
        self.rows[row_id].set_attributes(row_attributes)
        print("Row updated")
    except Exception as err:
      print(err)
    

  # Question 6 & 7
  # Time complexity : O(Number of rows)
  # Space complexity: O(Number of rows)
  def get_rows(self, count = -1):
    output = []
    if count == -1 or count > len(self.rows):
      for row_id in self.rows:
              output.append(self.get_dict_from_row(row_id))
      return output
    else:
        for row_id in self.rows:
          if count == 0:
            return output
          output.append(self.get_dict_from_row(row_id))
          count -= 1
        print("returning "," all " if count<=1 else count," rows from ",self.table_name,"  Table")
        return output
    

  # Question 8
    # Time complexity : O(NlogN)
    # N = Number of rows
  # Space complexity: O(Number of rows)
  def order_by(self,column,order="asc",count=-1):
    output = []
    try:
      if column != "id":
        self.does_column_exists(column)
      for row_id in self.rows:
        output.append(self.get_dict_from_row(row_id))

      output = sorted(output,key = lambda i: i[column], reverse = True if order != "asc" else False)
      
      return output[:count] if count < len(output) and count!=-1 else output 
    except Exception as err:
      print(err)


  # Question 9
    # Time complexity : O(Number of rows)
  # Space complexity: O(Number of rows)
  def group_by(self,column):
    output = {}
    try:
      self.does_column_exists(column)
      for row_id in self.rows:
        row_attributes = self.rows[row_id].get_attributes()
        output[row_attributes[column]] = output.get(row_attributes[column], 0) + 1
      return output
    except Exception as err:
      print(err)
  
  
  # Utility function
  def get_dict_from_row(self,row_id):
    dict = {}
    dict["id"] = row_id
    row_attributes = self.rows[row_id].get_attributes()

    for attribute in row_attributes:
      dict[attribute] = row_attributes[attribute]
    
    return dict

  # Utility function
  def does_column_exists(self,column):
    if column not in self.columns:
      raise Exception("Incorrect column name")
  
  # Utility function
  def get_table_name(self):
    return self.table_name
  
  # Utility function
  def get_columns(self):
    return self.columns

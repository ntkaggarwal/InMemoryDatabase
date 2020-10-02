# -*- coding: utf-8 -*-
"""
@author: nitika
"""

import datetime

class Row:
  row_id = None
  attributes = {}
  created_at = None
  updated_at = None
  
  def __init__(self, row_id, attributes):
    self.row_id = row_id
    self.attributes = attributes
    self.created_at = datetime.datetime.now()
    self.updated_at = datetime.datetime.now()
  
  def get_attributes(self):
    return self.attributes
  
  def set_attributes(self, attributes):
    self.attributes = attributes
  
  def get_row_id(self):
    return self.row_id
  
  def set_updated_at(self, updated_at = datetime.datetime.now()):
    self.updated_at = updated_at

  
  
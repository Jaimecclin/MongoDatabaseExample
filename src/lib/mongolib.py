#!/usr/bin/python3
 
import pymongo
import time

class DatabaseHandler():

  def __init__(self, server_path=None, db_name=None):
    t1 = time.time()
    self._client = pymongo.MongoClient("") # Need Database server url
    t2 = time.time()
    print(t2-t1)
    self._database = self._client['User']

  def _get_collection(self, collection_name):
    co = self._database[collection_name]
    return co

  def add(self, collection_name, column_name, data):
    co = self._get_collection(collection_name)
    return co.insert_one(data) 
    
  def find(self, collection_name, column_name):
    co = self._get_collection(collection_name)
    return co.find()
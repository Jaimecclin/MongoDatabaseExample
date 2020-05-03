#!/usr/bin/python3
 
from lib.mongolib import DatabaseHandler
 
db_handler = DatabaseHandler()

COLLECTION_NAME = 'users'
COL_ID = 'uid'
# db_handler.add(COLLECTION_NAME, COL_ID, {'abc': 123})
print(db_handler.find(COLLECTION_NAME, COL_ID))

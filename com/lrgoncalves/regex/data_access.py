import pymongo
from pymongo import MongoClient

import json

def insert(json):
    data_client = pymongo.MongoClient("mongodb://localhost:27017/")

    linkedin_db = data_client["linkedin"]

    print(data_client.list_database_names())

    profiles_col = linkedin_db["profiles"]

    print(linkedin_db.list_collection_names())

    json_valid = json_validator(json)
    
    if json_valid:
        profiles_col.insert_one(json)

def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False

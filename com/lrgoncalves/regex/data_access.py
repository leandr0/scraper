import pymongo
from pymongo import MongoClient
import json

def insert(json_profile):
    try:
        data_client = pymongo.MongoClient("mongodb://localhost:27017/")
    
        linkedin_db = data_client["linkedin"]
    
        profiles_col = linkedin_db["profiles"]
    
        json_valid = json_validator(json_profile)
        
        data = json.loads(str(json_profile))
        print("Inserting" + data)
        if json_valid:
            profiles_col.insert(data)
            
        data_client.close()
        
    except ValueError as error:
        print("Insert error: %s" % error)     

def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False

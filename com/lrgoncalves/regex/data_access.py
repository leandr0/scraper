import pymongo
from pymongo import MongoClient
import json

def insert(json_profile):
    try:
        data_client = pymongo.MongoClient("mongodb://localhost:27017/")
    
        linkedin_db = data_client["linkedin"]
    
        profiles_col = linkedin_db["profiles"]
    
        #print("json_validator")
        json_valid = json_validator(json_profile)
        
        #print("json_validator#json_valid >> " + json_valid)
        data = json.loads(json_profile)
        
        #print("Inserting" + data)
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
        print("[data_access.py#json_validator] >> invalid json: %s" % error)
        return False

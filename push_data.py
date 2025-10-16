import os
import sys
import json
import certifi

import pandas as pd
import numpy as np
import pymongo

from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging import logger

from dotenv import load_dotenv

#Load the environment...
load_dotenv()


MONGO_DB_URL = os.getenv("MONGO_DB_URL")

ca = certifi.where() 




class NetworkDataExtract():
    def __init__(self):
        try:
            pass

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def cv_to_json_convertor(self , file_path):
        try:
            data = pd.read_csv("D:/Network Security Project/Network_Data/phisingData.csv")

            data.reset_index(drop=True,inplace=True)

            #List of json Arrays....
            records = list(json.loads(data.T.to_json()).values())

            return records
    
        except Exception as e:
            raise NetworkSecurityException(e ,sys)

    def insert_data_mongodb(self , records , database ,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__ == "__main__":
    FILE_PATH = "D:/Network Security Project/Network_Data/phisingData.csv"
    DATABASE = "NishitAI"
    Collection = "NetworkData"
    netwrokobj = NetworkDataExtract()
    records = netwrokobj.cv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records = netwrokobj.insert_data_mongodb(records , DATABASE , Collection)
    print(no_of_records)
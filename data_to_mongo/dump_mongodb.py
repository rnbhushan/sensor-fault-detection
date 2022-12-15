print("Hi")
import pymongo
import pandas as pd
import json
import os
import sys
from dotenv import load_dotenv
load_dotenv()
client = pymongo.MongoClient(os.getenv("MONGODB_CREDENATIALS"))

print(os.getenv("MONGODB_CREDENATIALS"))

class Environmentvariables(object):
     def __init__(self):
        self.data_file_path = os.getenv("DATA_FILE_NAME")
        self.datbase_name = os.getenv("DATRABASE_NAME")
        self.collection_name = os.getenv("COLELCTION_NAME")
        

env = Environmentvariables()
print(env.data_file_path,"datafilename")
print(env.datbase_name,"databasename")

if __name__ == '__main__':
        df = pd.read_csv(env.data_file_path)
        print(f'Rows and columns in the data file :{df.shape}')
        df.reset_index(drop = True,inplace=True)
        json_records = list(json.loads(df.T.to_json()).values())
        # print(json_records[0])
        client[env.datbase_name][env.collection_name].insert_many(json_records)
        print("Data uploaded to mongo db successfully")












import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://shashi:sasidiv@ac-qknzvyo-shard-00-00.xt5e03i.mongodb.net:27017,ac-qknzvyo-shard-00-01.xt5e03i.mongodb.net:27017,ac-qknzvyo-shard-00-02.xt5e03i.mongodb.net:27017/?ssl=true&replicaSet=atlas-qss8nw-shard-0&authSource=admin&retryWrites=true&w=majority")

DATA_FILE_NEW = (r"/config/workspace/insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_NEW)
    print(f"Rows and Columns :{df.shape}")

    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())

    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


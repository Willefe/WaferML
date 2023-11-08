from pymongo.mongo_client import MongoClient
import os
import pandas as pd
import json


# get mongo url
uri = os.getenv("MONGO_DB_URL")

# create a new client and connect to a server
client = MongoClient(uri)

# create database name and collection name
MONGO_DATABASE_NAME = "wafer"
MONGO_COLLECTION_NAME = "sensor"

# read the data as a dataframe
df = pd.read_csv(
    r"C:\Users\Will\Desktop\MLProjectsPW\WaferML\notebooks\data\wafer.csv")
df = df.drop("Unnamed: 0", axis=1)

# convert the data into json
json_df = list(json.loads(df.T.to_json()).values())

# dump data into mongo_db
client[MONGO_DATABASE_NAME][MONGO_COLLECTION_NAME].insert_many(json_df)

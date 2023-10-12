import os
import sys

import boto3
import dill
import numpy as np
import pandas as pd

from pymongo import MongoClient

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from src.exception import CustomException

def export_collection_as_data_frame(collection_name, database_name):
    try:
        client = MongoClient(os.getenv("MONGO_DB_URL"))
        
        collection_name = client[database_name][collection_name]

        df = pd.DataFrame(list(collection_name.find()))
        
        if "_id" in df.columns.to_list():
            df = df.drop(columns=['_id'], axis=1)

        df.replace({"na":np.nan}, inplace=True)

        

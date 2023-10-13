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

        return df
    except Exception as e:
        raise CustomException(e, sys)


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    
    except Exception as e: 
        raise CustomException(e, sys)
    

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            obj = dill.load(file_obj)

        return obj
    except Exception as e:
        raise CustomException(e, sys)
    
def upload_file(from_filename, to_filename, bucket_name):
    try:
        s3_resource = boto3.resource('s3')
    
        s3_resource.meta.client.upload_file(from_filename, bucket_name, to_filename)
        
    except Exception as e:
        raise CustomException(e, sys)
    

def downlaod_model(bucket_name,bucket_filename, dest_filename):
    try:
        s3_client = boto3.client('s3')

        s3_client.download_file(bucket_name, bucket_filename, dest_filename)
        
        return dest_filename
    
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(X, y, models):
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.2, random_state=42)

        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)
            
            r2_train = r2_score(y_train, y_train_pred)

            r2_test = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = r2_test


        return report
    
    except Exception as e:
        raise CustomException(e, sys)
    
        

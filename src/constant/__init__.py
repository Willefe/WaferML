import os


AWS_S3_BUCKET_NAME = "wafersensor"
MONGO_DATABASE_NAME = "wafer"
MONGO_COLLECTION_NAME = "sensor"


TARGET_COLUMN = "quality"
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = "artifacts"

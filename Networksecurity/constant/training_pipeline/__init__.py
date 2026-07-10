import os 
import sys
import numpy as np
import pandas as pd

"""
Defining comman constant variable for Training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "NetworkData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

PREPROCESSING_OBJEST_FILE_NAME= "Preprocesssing.pkl"
MODEL_FILE_NAME= "model.pkl"
SCHEMA_FILE_PATH= os.path.join("data_schema", "schema.yaml")
SCHEMA_DROP_COLS= "drop_columns"

SAVED_MODEL_DIR= os.path.join("saved_models")

"""
Data Ingestion related constants start with DATA_INGESTION variable name
"""
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "Academy1"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

"""
Data validation related constants start with DATA_VALIDATION variable name
"""

"""
Data Transofmation related constants start with DATA_TRANSFORMATION variable name
"""

"""
Model Trainer related constants start with MODEL_TRAINER variable name
"""

"""
Model Evaluation related constants start with MODEL_EVALUATION variable name
"""


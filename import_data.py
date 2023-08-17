from pymongo.mongo_client import MongoClient
import pandas as pd
import json

from sklearn.datasets import load_breast_cancer

df = load_breast_cancer()

data = pd.DataFrame(df.data, columns = df.feature_names)
data['target'] = df.target

uri = "mongodb+srv://zaibreyaz:Password@cluster0.dfqgowm.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

DATABASE_NAME="Breast_Cancer_Assignment"
COLLECTION_NAME="Breast_Cancer"

json_record=list(json.loads(data.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
from pymongo.mongo_client import MongoClient
import pandas as pd
import json


#url
uri="mongodb+srv://surajdata45:surya2299@cluster0.gg8geft.mongodb.net/?appName=Cluster0"

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="sensors"
COLLECTION_NAME='waferfault'

df=pd.read_csv("C:\Users\suraj\Downloads\Sensor_Fault_Detection\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)



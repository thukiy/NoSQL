from fastapi import FastAPI
from app.routers import drivers

app = FastAPI()

from pymongo.mongo_client import MongoClient

uri = "mongodb://admin:secret@localhost:27017/"

client = MongoClient(uri)

try:    
    client.admin.command('ping')
    print("Pinged your deployment. You sucessfully connected to MongoDB")
except Exception as e:
    print(e)

import os
from pymongo import MangoClient
from dotenv import load_dotenv


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:secret@mongodb:27017/")
DB_NAME = os.getenv("DB_NAME", "f1_analysis")

client = MangoClient(MONGO_URI)
db = client[DB_NAME]

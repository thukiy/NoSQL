from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
def get_db():
    client = MongoClient(uri)
    return client["f1_analysis"]
from pymongo import AsyncMongoClient

uri = "mongodb://localhost:27017/"
async def get_db():
    client = AsyncMongoClient(uri)
    await client.aconnect()
    return client.get_database("f1_analysis")
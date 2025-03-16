from fastapi import FastAPI
import uvicorn
from app.routers import drivers, circuit, races, teams

app = FastAPI()

app.include_router(drivers.router)
app.include_router(circuit.router)
app.include_router(races.router)
app.include_router(teams.router)

from pymongo.mongo_client import MongoClient

uri = "mongodb://localhost:27017/"

client = MongoClient(uri)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)

def get_db():
    client = MongoClient(uri)
    return client["f1_analysis"]
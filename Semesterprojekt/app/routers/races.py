from fastapi import APIRouter
from app.database import db
from app.models import Race
from datetime import datetime 

app = APIRouter()

@app.get(("/races/"),response_model = list[Race])

async def get_races():
    races = list(db.races.find({}, ))
    return races

@app.post(("/races/"), response_model=Race)
async def create_races():
    new_races = await db.races.insert_one(races.dict())

@app.put(("/races/"), response_model=Race)
async def update_races():
    updated_race = db.races.update_one({})
    return updated_race
@app.delete("/races/")
async def delete_races()
    deleted_races = db.races.delete_one()
    return deleted_races 2
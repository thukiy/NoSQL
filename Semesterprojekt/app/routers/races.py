from fastapi import APIRouter, Body, Depends
from app.database import db
from app.models import Race, PyObjectId
from datetime import datetime 
from Semesterprojekt.main import get_db
from pymongo import database

router = APIRouter(dependencies=[Depends(get_db)])



# route to get all the drivers in the list

@router.get(("/races/"),response_model = list[Race])

async def get_races(db= Depends(get_db)):
    races = list(db.races.find({}, ))
    return races

@router.post(("/races/"), response_model=Race, )
async def create_races(race: Race=Body(...), db= Depends(get_db)):
    data = race.model_dump(by_alias=True, exclude = ["id"])
    new_race= await db["races"].insert_one(data)
    data["id"]=new_race.inserted_id
    return data

@router.put(("/races/{race_id}"), response_model=Race)
async def update_races(race_id: PyObjectId, race: Race=Body(...), db= Depends(get_db)):
    data = race.model_dump(by_alias=True, exclude = ["id"])
    new_race= await db["races"].update_one({'_id': race_id},data)
    data["id"]=race_id
    return data


@router.delete("/races/{race_id}", db= Depends(get_db))
async def delete_races(race_id: PyObjectId):
    deleted_races = db.races.delete({'_id': race_id})
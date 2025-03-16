from fastapi import APIRouter, Body, Depends
from app.models import Race, PyObjectId
from dependencies import get_db
from pymongo.database import Database

router = APIRouter(dependencies=[Depends(get_db)])



# route to get all the drivers in the list

@router.get(("/races/"), response_model = list[Race])

async def get_races(db: Database = Depends(get_db)):
    races = list(db.races.find({}, ))
    return races

@router.post(("/races/"), response_model=Race)
async def create_races(race: Race=Body(...), db: Database = Depends(get_db)):
    data = race.model_dump(by_alias=True, exclude = ["id"])
    new_race= await db["races"].insert_one(data)
    data["id"]=new_race.inserted_id
    return data

@router.put(("/races/{race_id}"), response_model=Race)
async def update_races(race_id: PyObjectId, race: Race=Body(...), db: Database = Depends(get_db)):
    data = race.model_dump(by_alias=True, exclude = ["id"])
    new_race= await db["races"].update_one({'_id': race_id},data)
    data["id"]=race_id
    return data


@router.delete("/races/{race_id}")
async def delete_races(race_id: PyObjectId, db: Database  = Depends(get_db)):
    deleted_races = db.races.delete({'_id': race_id})
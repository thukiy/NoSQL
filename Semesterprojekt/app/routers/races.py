from bson import ObjectId
from fastapi import APIRouter, Body, Depends
from app.models import Race, PyObjectId, LapTime
from dependencies import get_db
from pymongo.database import Database
from pymongo import ReturnDocument

router = APIRouter(dependencies=[Depends(get_db)])



# route to get all the drivers in the list

@router.get(("/races/"), response_model = list[Race])

async def get_races(db: Database = Depends(get_db)):
    races = await db.races.find({}).to_list()
    api_reponse = [Race(**race) for race in races]
    return api_reponse

@router.post(("/races/"), response_model=Race)
async def create_races(race: Race=Body(...), db: Database = Depends(get_db)):
    data = race.model_dump(by_alias=True, exclude = ["id"])
    new_race= await db["races"].insert_one(data)
    return Race(**data, id=new_race.inserted_id )

@router.post(("/races/{race_id}/laptime"), response_model=Race)
async def update_laptime(race_id: PyObjectId, laptime: LapTime=Body(...), db: Database = Depends(get_db)):
    data = laptime.model_dump(by_alias=True)
    updated_race= await db["races"].find_one_and_update(filter={'_id': ObjectId(race_id)}, update={'$push':{"lap_times": data}}, return_document = ReturnDocument.AFTER)
    return Race(**updated_race)

@router.put(("/races/{race_id}"), response_model=Race)
async def update_race(race_id: PyObjectId, race:Race, db:Database=Depends(get_db)):
    data = race.model_dump(by_alias=True, exclude= ["id"])
    updating_race = await db["races"].find_one_and_update(filter={"_id": ObjectId(race_id)}, update={'$set':data},return_document=ReturnDocument.AFTER)
    return updating_race


@router.delete("/races/{race_id}")
async def delete_races(race_id: PyObjectId, db: Database  = Depends(get_db)):
    deleted_races = await db.races.delete_one({"_id": ObjectId(race_id)})
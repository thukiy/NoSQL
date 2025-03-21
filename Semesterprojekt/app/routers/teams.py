from bson import ObjectId
from fastapi import APIRouter, Body, Depends
from app.models import Team, PyObjectId
from dependencies import get_db
from pymongo.database import Database
from pymongo import ReturnDocument

router = APIRouter(dependencies=[Depends(get_db)])

@router.get(("/teams/"),response_model = list[Team])
async def get_teams(db: Database = Depends(get_db)):
    teams = await db.teams.find({}).to_list()
    api_response = [Team(**team) for team in teams]
    return api_response

@router.post(("/teams/"), response_model=Team)
async def create_team(team: Team=Body(...), db: Database = Depends(get_db)):
    data = team.model_dump(by_alias=True, exclude = ["id"])
    new_team = await db["teams"].insert_one(data)
    api_response = Team(**data, id=new_team.inserted_id)
    return api_response

@router.put(("/teams/{team_id}"), response_model=Team)
async def update_team(team_id: PyObjectId, team: Team=Body(...), db: Database = Depends(get_db) ):
    data = team.model_dump(by_alias=True, exclude = ["id"])
    update_team = await db["teams"].find_one_and_update(filter={"_id": ObjectId(team_id)}, update={'$set': data}, return_document=ReturnDocument.AFTER)
    return update_team


@router.delete("/teams/{team_id}")
async def delete_team(team_id: PyObjectId, db: Database = Depends(get_db)):
    deleted_team = await db.teams.delete_one({"_id": ObjectId(team_id)})



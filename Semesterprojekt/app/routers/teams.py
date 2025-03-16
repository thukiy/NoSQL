from typing import Annotated
from bson import ObjectId
from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel
from app.database import db
from app.models import Team, PyObjectId
from Semesterprojekt.main import get_db
from pymongo import database


router = APIRouter(dependencies=[Depends(get_db)])

@router.get(("/teams/"),response_model = list[Team])

async def get_teams(db= Depends(get_db)):
    teams = list(db.teams.find({},{"id": 0} ))
    return teams

@router.post(("/teams/"), response_model=Team)
async def create_team(team: Team=Body(...), db= Depends(get_db)):
    data = team.model_dump(by_alias=True, exclude = ["id"])
    new_team= await db["teams"].insert_one(data)
    data["id"]=new_team.inserted_id
    return data

@router.put(("/teams/{team_id}"), response_model=Team)
async def update_team(team_id: PyObjectId, team: Team=Body(...),db= Depends(get_db) ):
    data = team.model_dump(by_alias=True, exclude = ["id"])
    new_team = await db["teams"].update_one({'_id': team_id},data)
    data["id"]=team_id
    return data


@router.delete("/teams/{team_id}")
async def delete_team(team_id: PyObjectId, db= Depends(get_db)):
    deleted_team = db.team.delete({'_id': team_id})



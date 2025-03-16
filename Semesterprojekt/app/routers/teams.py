from fastapi import APIRouter, Body, Depends
from app.models import Team, PyObjectId
from dependencies import get_db
from pymongo.database import Database

router = APIRouter(dependencies=[Depends(get_db)])

@router.get(("/teams/"),response_model = list[Team])
async def get_teams(db: Database = Depends(get_db)):
    teams = list(db.teams.find({},{"id": 0} ))
    return teams

@router.post(("/teams/"), response_model=Team)
async def create_team(team: Team=Body(...), db: Database = Depends(get_db)):
    data = team.model_dump(by_alias=True, exclude = ["id"])
    new_team= await db["teams"].insert_one(data)
    data["id"]=new_team.inserted_id
    return data

@router.put(("/teams/{team_id}"), response_model=Team)
async def update_team(team_id: PyObjectId, team: Team=Body(...), db: Database = Depends(get_db) ):
    data = team.model_dump(by_alias=True, exclude = ["id"])
    new_team = await db["teams"].update_one({'_id': team_id}, data)
    data["id"]=team_id
    return data


@router.delete("/teams/{team_id}")
async def delete_team(team_id: PyObjectId, db: Database = Depends(get_db)):
    deleted_team = db.team.delete({'_id': team_id})



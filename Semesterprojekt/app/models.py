from typing import Annotated, Optional
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field, AfterValidator
import uuid 
from datetime import datetime



def check_object_id(value: str) -> str:
    if not ObjectId.is_valid(value):
        raise ValueError('Invalid ObjectId')
    return value

PyObjectId = Annotated[str, AfterValidator(check_object_id)]

class BaseEntity(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)

class LapTime(BaseModel):
    driver_id: str
    lap_number: int
    time: float

class Race(BaseEntity):
    name: str
    season: int
    race_number: int
    circuit_id: str
    date: datetime
    laps: int 
    lap_times:list[LapTime]

class Circuit(BaseEntity):
    name: str
    location: str
    country: str
    length_km: float
    turns: int

class Team(BaseEntity):
    name: str
    chassis: str
    power_unit: str
    team_principal: str

class Driver(BaseEntity):
    name: str
    team_id: str
    nationality: str
    birth_date: datetime
    car_number: int





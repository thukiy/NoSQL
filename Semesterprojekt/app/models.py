from typing import Annotated, Optional
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field, BeforeValidator
import uuid 
from datetime import datetime



def objectid_to_str(value) -> str:
    if isinstance(value, ObjectId):
        return str(value)
    if isinstance(value, str) and ObjectId.is_valid(value):
        return value
    raise ValueError("Invalid ObjectId")

PyObjectId = Annotated[str, BeforeValidator(objectid_to_str)]

class BaseEntity(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)

class LapTime(BaseModel):
    driver_id: PyObjectId
    lap_count: int
    time: float

class Race(BaseEntity):
    name: str
    season: int
    race_number: int
    circuit_id: PyObjectId
    date: datetime
    laps: int 
    lap_times: list[LapTime] = Field(default=[])

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
    team_id: PyObjectId
    nationality: str
    birth_date: datetime
    car_number: int





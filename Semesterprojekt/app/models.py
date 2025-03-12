from pydantic import BaseModel, ConfigDict
import uuid 
from datetime import datetime

class Race(BaseModel):
    id: str
    name: str
    season: int
    round: int
    circuit_id: str
    date: datetime
    laps: int

class Circuit(BaseModel):
    id: str
    name: str
    location: str
    country: str
    length_km: float
    turns: int

class Team(BaseModel):
    id: str
    name: str
    chassis: str
    power_unit: str
    team_principal: str

class Driver(BaseModel):
    id: str
    name: str
    team_id: str
    nationality: str
    birth_date: datetime
    car_number: int

class LapTime(BaseModel):
    id: str
    race_id: str
    driver_id: str
    lap_number: int
    time: float



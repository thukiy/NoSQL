from typing import Annotated
from bson import ObjectId
from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel, Field, AfterValidator, BeforeValidator
from app.database import db
from app.models import Circuit, PyObjectId
from datetime import datetime
from Semesterprojekt.main import get_db
from pymongo import database


router = APIRouter(dependencies=[Depends(get_db)])



# route to get all the drivers in the list
@router.get(("/circuit/"), response_model=list[Circuit])

async def get_circuits(db= Depends(get_db)):
    circuits = list(db.circuits.find({}, {"_id": 0}))
    return circuits

# route to create new drivers
@router.post(("/circuit/"), response_model=Circuit)
async def create_circuit(circuit:Circuit=Body(...), db= Depends(get_db)):
    data = circuit.model_dump(by_alias=True, exclude = ["id"])
    new_circuit= await db["circuit"].insert_one(data)
    data["id"]=new_circuit.inserted_id
    return data

#route to update an existing driver by its ID
@router.put(("/circuit/"), response_model=Circuit)
async def update_drivers(circuit_id: PyObjectId, circuit: Circuit, db= Depends(get_db)):
    data = circuit.model_dump(by_alias=True, exclude = ["id"])
    new_item= await db["circuit"].update_one({'id': circuit_id}, data)
    data["id"]=circuit_id
    return data

#route to delete a driver by it ID
@router.delete("/circuit/{circuit_id}")
async def delete_circuit(circuit_id: PyObjectId, db= Depends(get_db)):
    del_circuit = await db.circuit.delete({'_id': circuit_id})
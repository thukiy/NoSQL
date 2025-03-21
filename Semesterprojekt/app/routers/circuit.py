from bson import ObjectId
from fastapi import APIRouter, Body, Depends
from app.models import Circuit, PyObjectId
from dependencies import get_db
from pymongo.database import Database
from pymongo import ReturnDocument

router = APIRouter(dependencies=[Depends(get_db)])



# route to get all the circuits in the list
@router.get(("/circuit/"), response_model=list[Circuit])

async def get_circuits(db: Database = Depends(get_db)):
    circuits = await db.circuit.find({}).to_list()
    api_response = [Circuit(**circuit) for circuit in circuits]
    return api_response

# route to create new circuit
@router.post(("/circuit/"), response_model=Circuit)
async def create_circuit(circuit:Circuit=Body(...), db: Database = Depends(get_db)):
    data = circuit.model_dump(by_alias=True, exclude = ["id"])
    new_circuit= await db["circuit"].insert_one(data)
    return Circuit(**data, id=new_circuit.inserted_id)

#route to update an existing circuit by its ID
@router.put(("/circuit/{circuit_id}"), response_model=Circuit)
async def update_drivers(circuit_id: PyObjectId, circuit: Circuit, db: Database = Depends(get_db)):
    data = circuit.model_dump(by_alias=True, exclude = ["id"])
    updated_circuit= await db["circuit"].find_one_and_update(filter={"_id": ObjectId(circuit_id)}, update={'$set': data}, return_document=ReturnDocument.AFTER)
    return updated_circuit

#route to delete a circuit by it ID
@router.delete("/circuit/{circuit_id}")
async def delete_circuit(circuit_id: PyObjectId, db: Database = Depends(get_db)):
    del_circuit = await db.circuit.delete_one({'_id': ObjectId(circuit_id)})
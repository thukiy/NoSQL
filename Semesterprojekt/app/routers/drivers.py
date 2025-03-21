from bson import ObjectId
from fastapi import APIRouter, Body, Depends
from app.models import Driver, PyObjectId
from dependencies import get_db
from pymongo.database import Database
from pymongo import ReturnDocument

router = APIRouter(dependencies=[Depends(get_db)])


# route to get all the drivers in the list
@router.get(("/drivers/"), response_model=list[Driver])
async def get_drivers(db: Database = Depends(get_db)):
    drivers = await db.drivers.find({}).to_list()
    api_response = [Driver(**driver) for driver in drivers]
    return api_response


# route to create new drivers
@router.post(("/drivers/"), response_model=Driver)
async def create_drivers(driver: Driver = Body(...), db: Database = Depends(get_db)):
    data = driver.model_dump(by_alias=True, exclude = ["id"])
    new_item= await db["drivers"].insert_one(data)
    return Driver(**data, id=new_item.inserted_id)

#route to update an existing driver by its ID
@router.put(("/drivers/{driver_id}"), response_model=Driver)
async def update_drivers(driver_id: PyObjectId, driver: Driver, db: Database = Depends(get_db)):
    data = driver.model_dump(by_alias=True, exclude = ["id"])
    update_drivers = await db["drivers"].find_one_and_update(filter={"_id": ObjectId(driver_id)}, update={'$set': data}, return_document = ReturnDocument.AFTER)
    return update_drivers

#route to delete a driver by its ID
@router.delete("/drivers/{driver_id}")
async def delete_drivers(driver_id: PyObjectId, db: Database = Depends(get_db)):
    del_drivers = await db.drivers.delete_one({"_id": ObjectId(driver_id)})
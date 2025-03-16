from fastapi import APIRouter, Body, Depends
from app.models import Driver, PyObjectId
from dependencies import get_db
from pymongo.database import Database


router = APIRouter(dependencies=[Depends(get_db)])


# route to get all the drivers in the list
@router.get(("/drivers/"), response_model=list[Driver])
async def get_drivers(db: Database = Depends(get_db)):
    drivers = list(db.drivers.find({}, {"_id": 0}))
    return drivers

# route to create new drivers
@router.post(("/drivers/"), response_model=Driver)
async def create_drivers(driver: Driver = Body(...), db: Database = Depends(get_db)):
    data = driver.model_dump(by_alias=True, exclude = ["id"])
    new_item= await db["drivers"].insert_one(data)
    data["id"]=new_item.inserted_id
    return data

#route to update an existing driver by its ID
@router.put(("/drivers/"), response_model=Driver)
async def update_drivers(driver_id: PyObjectId, driver: Driver, db: Database = Depends(get_db)):
    data = driver.model_dump(by_alias=True, exclude = ["id"])
    new_item= await db["drivers"].update_one({'id': driver_id}, data)
    data["id"]=driver_id
    return data

#route to delete a driver by it ID
@router.delete("/driver/{driver_id}")
async def delete_drivers(driver_id: PyObjectId, db: Database = Depends(get_db)):
    del_drivers = await db.drivers.delete({'_id': driver_id})
from fastapi import APIRouter
from app.database import db
from app.models import Driver
from datetime import datetime


app = APIRouter()

# route to get all the drivers in the list
@app.get(("/drivers/"), response_model=list[Driver])

async def get_drivers():
    drivers = list(db.drivers.find({}, {"_id": 0}))
    return drivers

# route to create new drivers
@app.post(("/drivers/"), response_model=Driver)
async def create_drivers():
    new_drivers = await db.drivers.insert_one(drivers.dict())

#route to update an existing driver by its ID
@app.put(("/drivers/"), response_model=Driver)
async def update_drivers():
    updated_drivers = db.drivers.updateOne({})
    return updated_drivers

#route to delete a driver by it ID
@app.delete("/driver/{driver_id}")
async def delete_drivers(driver_id: int):
    del_drivers = await db.drivers.delete()
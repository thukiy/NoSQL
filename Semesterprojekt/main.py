from fastapi import FastAPI
import uvicorn
from app.routers import drivers, circuit, races, teams

app = FastAPI()

app.include_router(drivers.router)
app.include_router(circuit.router)
app.include_router(races.router)
app.include_router(teams.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)


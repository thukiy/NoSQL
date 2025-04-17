from fastapi import FastAPI
import uvicorn
from app.routers import drivers, circuit, races, teams

app = FastAPI(
    title = "F1 API",
    description=" API to manage F1 races"

)


app.include_router(drivers.router)
app.include_router(circuit.router)
app.include_router(races.router)
app.include_router(teams.router)


@app.get("/")
def home():
    return {"message": "Welcome to the F1 API"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
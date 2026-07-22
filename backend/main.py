from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#rememebr to import these routes and models to the main.py file
from models.tank_profile import TankProfile 
from models.user_profile import User
from routes.tank_routes import router as tank_router
from routes.user_routes import router as user_router
from routes.waterlog_routes import router as water_log_router

# import db after the features routes and models
from sqlmodel import SQLModel  
from database.db import engine


# note to self this runs the db without it mag 404 or null imo mga http pls make actual notes and shi
@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)  #database
    yield



app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tank_router, prefix="/tanks", tags=["Tanks"])
app.include_router(water_log_router, prefix="/tanks", tags=["Water Logs"])
app.include_router(user_router, prefix="/users", tags=["Users"])


@app.get("/")
def root():
    return {"message": "BANGUS BUHAI"}
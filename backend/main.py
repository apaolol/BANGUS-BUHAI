from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel  # 👈 Added this import

from database.db import engine
from models.tank_profile import TankProfile
from routes.tank_routes import router as tank_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs BEFORE the app starts accepting requests
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


@app.get("/")
def root():
    return {"message": "BANGUS BUHAI"}
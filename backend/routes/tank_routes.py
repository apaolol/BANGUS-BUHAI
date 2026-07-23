from fastapi import APIRouter, Depends, status
from models.tank_profile import CreateTankProfile, TankProfile
import services.tank_services as service

from sqlmodel import Session
from database.db import get_session


router = APIRouter()

# create tank profike
@router.post("/", response_model=TankProfile, status_code=status.HTTP_201_CREATED)
def create_tank(tank_profile: CreateTankProfile, db: Session = Depends(get_session)):
    return service.create_tank(tank_profile=tank_profile, db=db)

# get all tanks
@router.get("/", response_model=list[TankProfile], status_code=status.HTTP_200_OK)
def get_all_tanks(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    return service.get_all_tanks(skip=skip, limit=limit, db=db)

# specific one tank onleh
@router.get("/{tank_id}", response_model=TankProfile, status_code=status.HTTP_200_OK)
def view_tank(tank_id: int, db: Session = Depends(get_session)):
    return service.view_tank(tank_id=tank_id, db=db)

#update one tank
@router.put("/{tank_id}", response_model=TankProfile, status_code=status.HTTP_200_OK)
def update_tank(
    tank_id: int, tank_data: CreateTankProfile, db: Session = Depends(get_session)
    ):

    return service.update_tank(tank_id=tank_id, tank_data=tank_data, db=db)

@router.delete("/{tank_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tank(tank_id: int, db: Session = Depends(get_session)):

    return service.delete_tank(tank_id=tank_id, db=db)

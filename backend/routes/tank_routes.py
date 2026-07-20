from fastapi import APIRouter, Depends, HTTPException
from models.tank_profile import TankProfile
from database.db import get_session
from sqlmodel import Session, select


router = APIRouter()

# create tank profike
@router.post("/")
def create_tank(tank_profile: TankProfile, db: Session = Depends(get_session)):
    # Logic to create a new tank profile in
    tank_profile.capacity = tank_profile.volume_ml * 600

    db.add(tank_profile)
    db.commit()
    #db.refresh(tank_profile)
    return {"message": "Tank Profile Successfully  Added"}

# get all tanks
@router.get("/", response_model=list[TankProfile])
def get_all_tanks(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_session)
    ):
    # Logic to retrieve all tanks from the database
    tanks = db.exec(
        select(TankProfile)
        .offset(skip)
        .limit(limit)).all()
    return tanks

# specific one tank onleh
@router.get("/{tank_id}", response_model=TankProfile)
def view_tank(tank_id: int, db: Session = Depends(get_session)):
    # Logic to retrieve
    tank = db.get(TankProfile, tank_id)
    if not tank:
        raise HTTPException(status_code=404, detail="Tank not found")
    return tank

#update one tank
@router.put("/{tank_id}")
def update_tank(
    tank_id: int, tank_data: TankProfile, db: Session = Depends(get_session)
    ):
    # Logic to update an existing tank profile
    tank = db.get(TankProfile, tank_id)
    if not tank:
        raise HTTPException(status_code=404, detail="Tank not Found")
    
    # update logic
    for key, val in tank_data.model_dump(exclude={"id", "capacity"}).items():
        setattr(tank, key, val)

    tank.capacity = tank.volume_ml * 600

    db.commit()
    db.refresh(tank)

    return {"message": "Tank updated successfully!"}

@router.delete("/{tank_id}")
def delete_tank(tank_id: int, db: Session = Depends(get_session)):
    # Logic to delete a tank profile
    tank = db.get(TankProfile, tank_id)
    if not tank:
        raise HTTPException(status_code=404, detail="Tank not Found")
    db.delete(tank)
    db.commit()

    return {"message": "Tank deleted successfully!"}

from fastapi import HTTPException
from models.tank_profile import TankProfile
from sqlmodel import Session, select

# create tank profike
def create_tank(tank_profile: TankProfile, db: Session):
    # Logic to create a new tank profile in
    tank_profile.capacity = tank_profile.volume_ml * 600

    db.add(tank_profile)
    db.commit()
    db.refresh(tank_profile)
    return tank_profile

# get all tanks
def get_all_tanks(
     db: Session, skip: int = 0, limit: int = 10):
    # Logic to retrieve all tanks from the database
    tanks = db.exec(
        select(TankProfile)
        .offset(skip)
        .limit(limit)).all()
    return tanks

# specific one tank onleh
def view_tank(tank_id: int, db: Session):
    # Logic to retrieve
    tank = db.get(TankProfile, tank_id)
    if not tank:
        raise HTTPException(status_code=404, detail="Tank not found")
    return tank

#update one tank
def update_tank(
    tank_id: int, tank_data: TankProfile, db: Session
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

    return tank


def delete_tank(tank_id: int, db: Session):
    # Logic to delete a tank profile
    tank = db.get(TankProfile, tank_id)
    if not tank:
        raise HTTPException(status_code=404, detail="Tank not Found")
    db.delete(tank)
    db.commit()

    return {"message": "Tank deleted successfully!"}

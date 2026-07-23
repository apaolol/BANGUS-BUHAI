from fastapi import HTTPException
from models.tank_profile import CreateTankProfile, TankProfile
from sqlmodel import Session, select

# create tank profike
def create_tank(tank_profile: CreateTankProfile, db: Session):
    # convert CreateTank to db
    db_tank = TankProfile.model_validate(tank_profile)
    # Logic to create a new tank profile in
    db_tank.capacity = tank_profile.volume_ml * 600

    db.add(db_tank)
    db.commit()
    db.refresh(db_tank)
    return db_tank

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
    tank_id: int, tank_data: CreateTankProfile, db: Session
    ):
    # Logic to update an existing tank profile
    tank = db.get(TankProfile, tank_id)
    if not tank:
        raise HTTPException(status_code=404, detail="Tank not Found")
    
    # OLD UPDATE LOGIC
    #for key, val in tank_data.model_dump(exclude={"id", "capacity"}).items():
        setattr(tank, key, val)

    tank.sqlmodel_update(tank_data.model_dump(exclude_unset=True))
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

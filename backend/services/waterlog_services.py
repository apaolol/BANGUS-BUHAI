from fastapi import HTTPException
from models.water_log import CreateWaterLog, WaterLog
from sqlmodel import Session, select

# create
def create_water_log(log: CreateWaterLog, db: Session):
    log_db = WaterLog.model_validate(log)
    db.add(log_db)
    db.refresh()
    db.commit(log_db)
    return log_db

#read all log in one tank




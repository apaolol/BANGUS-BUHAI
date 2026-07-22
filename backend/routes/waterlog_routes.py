from fastapi import APIRouter, Depends, status
from models.water_log import WaterLog
import services.waterlog_services as service

from sqlmodel import Session
from database.db import get_session

router = APIRouter()

# create log entry
@router.post("/{tank_id}", response_model=WaterLog, status_code=status.HTTP_201_CREATED)
def create_water_log(tank_id: tank_id, waterlog: WaterLog, db: Session = Depends(get_session)):
    return 

# view all logs for 
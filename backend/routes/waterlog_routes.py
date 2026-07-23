from fastapi import APIRouter, Depends, status
from models.water_log import CreateWaterLog, WaterLog
import services.waterlog_services as service

from sqlmodel import Session
from database.db import get_session

router = APIRouter()

# create log entry when creating it [pag default model mangayo sha tank id and id which sa atong json di required so mao]
@router.post("/{tank_id}/logs", response_model=WaterLog, status_code=status.HTTP_201_CREATED)
def create_water_log(tank_id: int, waterlog: CreateWaterLog, db: Session = Depends(get_session)):
    return 


# view all logs in all tanks
# must be defined before tank_id
#be conscious when making two same http req when it comes to decorators kai basin mag err 402
#static routes first( kanang walay {})
@router.get("/logs/all", response_model= list[WaterLog],status_code=status.HTTP_200_OK)
def get_all_logs(db: Session = Depends(get_session)):
    return

# view all logs for one tank
@router.get("/{tank_id}/logs", response_model=list[WaterLog], status_code=status.HTTP_200_OK)
def get_all_logs_for_tank(tank_id: int, skip: int = 0, limit: int =10, db: Session = Depends(get_session)):
    return

#view a log from one tank
@router.get("/{tank_id}/logs/{log_id}", response_model=WaterLog, status_code=status.HTTP_200_OK)
def get_log(tank_id: int, log_id: int, db: Session = Depends(get_session)):
    return

# update a log from one tank
@router.put("/{tank_id}/logs/{log_id}", response_model = WaterLog, status_code=status.HTTP_200_OK)
def update_log(tank_id: int, log_id: int, log_data: CreateWaterLog, db: Session = Depends(get_session)):
    return

# delete a log
@router.delete("/{tank_id}/logs/{log_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_log(tank_id: int, log_id: int, db: Session = Depends(get_session)):
    return
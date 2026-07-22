from fastapi import APIRouter, Depends, status
from models.user_profile import User
import services.user_services as service
from sqlmodel import Session
from database.db import get_session

router = APIRouter()

# create user profike
@router.post("/", response_model= User, status_code=status.HTTP_201_CREATED)
def create_user(user: User, db: Session = Depends(get_session)):
    return service.create_user(user=user, db=db)

# read all
@router.get("/", response_model = list[User])
def get_all_users(skip: int = 0, limit: int = 10, 
                  db: Session = Depends(get_session)):
    return service.get_all_users(skip=skip, limit=limit, db=db)

# read one
@router.get("/{user_id}", response_model = User)
def get_user(id: int, db: Session = Depends(get_session)):
    return service.get_user(id=id, db=db)

# update one
@router.put("/{user_id}", response_model = User)
def update_user(id: int, user_data: User, db: Session = Depends(get_session)):
    return service.update_user(id=id, user_data=user_data, db=db)


#delete user
@router.delete("/{user_id}")
def delete_user(id: int, db: Session = Depends(get_session)):
    return service.delete_user(id=id, db=db)

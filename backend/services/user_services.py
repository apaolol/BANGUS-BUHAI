from fastapi import HTTPException
from models.user_profile import User
from sqlmodel import Session, select

# create
def create_user(user: User, db: Session):
    # Logic to create a new user in the
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# read all
def get_all_users(db: Session, skip: int = 0, limit: int = 10):
    users = db.exec(
        select(User)
        .offset(skip)
        .limit(limit)).all()
    return users

# read one
def get_user(id: int, db: Session):
    user = db.get(User, id)
    if not user:
        raise HTTPException(status_code=404, details="User Not Found")
    return user

# update user
def update_user(id: int, user_data: User, db: Session):
    user = db.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    
    for key, val in user_data.model_dump(exclude={"id"}).items():
        setattr(user, key, val)
    db.commit()
    db.refresh(user)
    return user

# delete user
def delete_user(id: int, db: Session):
    user = db.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    db.delete(user)
    db.commit()
    return {"message" : "User delete succesfully"}
    



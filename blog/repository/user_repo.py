from sqlalchemy.orm import Session
from blog import schemas, models
from blog.database import get_db    
from fastapi import Depends, HTTPException
from blog.utils import hashing

def get_all_users(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

def get_user_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def create_user(request: schemas.UserCreate, db: Session):
    existing_user = db.query(models.User).filter(models.User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hashing.hash_password(request.password)  # Password should be hashed in the router
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(id: int, request: schemas.UserCreate, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = request.name
    user.email = request.email
    user.password = hashing.hash_password(request.password)  # Password should be hashed in the router

    db.commit()
    db.refresh(user)
    return {"data": "User updated successfully", "user": user}

def delete_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"data": "User deleted successfully"}

# Note: The hashing of the password should be done in the router or in a service layer before saving to the database.
# This ensures that the password is not stored in plain text.
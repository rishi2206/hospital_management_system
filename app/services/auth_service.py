from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.models.users import Users

from app.curd import user,role
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

def register_user(db: Session, user_data: UserCreate):
    
    existing_user = user.get_user_by_email(
        db,
        user_data.email
    )
    
    if existing_user:
        raise ValueError("Email already exists")
    
    existing_role = role.get_role_by_id(
        db,
        user_data.role_id
    )
    
    if not existing_role:
        raise ValueError("Invalid role")
    
    hashed_password = hash_password(
        user_data.password
    )
    
    new_user = Users(
        username = user_data.username,
        email = user_data.email,
        hashed_password = hashed_password,
        role_id = user_data.role_id
    )
    
    return user.create_user(
        db,
        new_user
    )
    

def login_user(db:Session , login_data:UserLogin):
    
    user_obj = user.get_user_by_email(
        db,
        login_data.email
    )
    
    if not user_obj:
        raise ValueError("Invalid email or password")
    
    if not verify_password(
        login_data.hashed_password,
        user_obj.hashed_password
    ):
        raise ValueError("Invalid email or password")
    
    token = create_access_token(
        {
            "sub": str(user_obj.id)
        }
    )
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }
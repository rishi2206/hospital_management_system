from sqlalchemy.orm import Session

from app.schemas.user import UserUpdate
from app.crud import user
from app.core.security import hash_password


def get_all_users(db: Session):
    return user.get_all_users(db)

def get_user_by_id(db: Session, user_id):
    user_obj = user.get_user_by_id(db,user_id)
    
    if not user_id:
        raise ValueError("User not Found")
    
    return user_obj

def update_user(db: Session, user_id, user_data: UserUpdate):
    user_obj = user.get_user_by_id(db, user_id)

    if not user_obj:
        raise ValueError("User not found")

    if user_data.username:
        user_obj.username = user_data.username

    if user_data.email:
        user_obj.email = user_data.email

    if user_data.password:
        user_obj.hashed_password = hash_password(user_data.password)

    if user_data.role_id:
        user_obj.role_id = user_data.role_id
        
    return user.update_user(db, user_obj)


def delete_user(db: Session, user_id):
    user_obj = user.get_user_by_id(db, user_id)

    if not user_obj:
        raise ValueError("User not found")

    user.delete_user(db, user_obj)

    return {
        "message": "User deleted successfully"
    }
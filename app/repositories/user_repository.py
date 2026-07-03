from sqlalchemy.orm import Session
from app.models.users import Users

def get_by_email(db: Session,email: str):
    return db.query(Users).filter(Users.email == email).first()


def get_by_id(db: Session, user_id):
    return db.query(Users).filter(Users.id == user_id).first()


def get_all(db: Session):
    return db.query(Users).all()


def create(db: Session, user: Users):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update(db: Session,user: Users):
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, user: Users):
    db.delete(user)
    db.commit()
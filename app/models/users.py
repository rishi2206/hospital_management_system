import uuid
from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Users(Base):
    __tablename__="users"
    
    id = Column(Integer,primary_key=True,nullable=False,index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, index=true, nullable=False)
    hashed_password = Column(String, nullable=False)
    role_id = Column(
        UUID(as_uuid=True),
        ForeignKey("roles.id")
    )
    is_active = Column(Boolean, nullable=False, default=True)
    created_at =  Column(
        DateTime,
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        default=datatime.utcnow,
        onupdate=datetime.utcnow
    )
    
    role = relationship("Role",back_populates="users")
    doctor = relationship("Doctor",back_populates="users",uselist=False)
    patient = relationship("Patient", back_populates="users", uselist=False)    
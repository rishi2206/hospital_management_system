import uuid
from sqlalchemy import Column, String, Integer, Date, Foreignkey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy.orm import relationship

from app.database import Base


class Doctor(Base):
    __tablename__="doctors"
    
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    user_id = Column(
        UUID(as_uuid=True),
        Foreignkey("users.id"),
        nullable=False
    )
    name = Column(String(100), nullable=False)
    specialization = Column(String(100), nullable=False)
    Phone_number = Column(String(15), nullable=False)
    email = Column(String(100), unique=True, index=true, nullable=False)
    department = Column(String(100), nullable=False)
    years_of_experience=Column(Integer, nullable=False)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    
    appointments =relationship("Appointment",back_populates="doctor")
import uuid
from sqlalchemy import Column, String, Integer, Date, Foreignkey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy.orm import relationship

from app.database import Base


class Patient(Base):
    __tablename__="patients"
    
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
    name = Column(String(50), nullable=False)
    Gender = Column(String(20), nullable=False)
    Age = Column(Integer, nullable=False)
    Phone_number = Column(String(15), nullable=False)
    email = Column(String(100), unique=True, index=true, nullable=False)
    blood_group = Column(String(5), nullable=True)
    emergency_contact = Column(String(15), nullable=True)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    
    appointments = relationship("Appointment", back_populates="patients") 
import uuid
from sqlalchemy import Column, String, Integer, Date, Time, Boolean, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy.orm import relationship

from app.database import Base


class Appointment(Base):
    __tablename__="appointments"
    
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    patient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("patients.id"),
        nullable=False
    )
    doctor_id = Column(
        UUID(as_uuid=True),
        ForeignKey("doctors.id"),
        nullable=False
    )
    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(Time, nullable=False)
    status = Column(String(30), nullable=False, default="Scheduled")
    notes = Column(Text, nullable=True)
    created_at=Column(
        DateTime,
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    
    patient = relationship("Patient", back_populates="appointment")
    doctor = relationship("Doctor",back_populates="appointments")
    
import uuid
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from app.database import Base

class Prescription(Base):
    __tablename__ = "prescriptions"
    
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    patient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("patients.id")
    )
    doctor_id = Column(
        UUID(as_uuid=True),
        ForeignKey("doctors.id")
    )
    appointment_id = Column(
        UUID(as_uuid=True),
        ForeignKey("appointments.id")
    )
    instructions = Column(Text, nullable=True)
    created_at = Column(
        DataTime,
        default=datatime.utcnow
    )
    updated_at = Column(
        DataTime,
        default=datatime.utcnow,
        onupdate=datatime.utcnow
    )
    
    patient = relationship("Patient", back_populates="prescription")
    doctor = relationship("Doctor", back_populates="prescription")
    appointment = relationship("Appointment", back_populates="prescription")
    items = relationship("Prescription_items", back_populates="prescription")

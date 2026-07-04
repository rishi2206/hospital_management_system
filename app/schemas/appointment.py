from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class AppointmentCreate(BaseModel):
    patient_id: UUID
    doctor_id: UUID
    appointment_date: datetime
    reason: str


class AppointmentResponse(BaseModel):
    id: UUID
    patient_id: UUID
    doctor_id: UUID
    appointment_date: datetime
    reason: str
    status: str

    class Config:
        from_attributes = True
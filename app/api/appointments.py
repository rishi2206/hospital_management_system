from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.database import get_db
from app.models.appointments import Appointment
from app.schemas.appointment import AppointmentCreate, AppointmentResponse

router = APIRouter(prefix="/appointments", tags=["Appointments"])


# ➤ Create Appointment
@router.post("/", response_model=AppointmentResponse)
def create_appointment(data: AppointmentCreate, db: Session = Depends(get_db)):
    new_appointment = Appointment(
        patient_id=data.patient_id,
        doctor_id=data.doctor_id,
        appointment_date=data.appointment_date,
        reason=data.reason,
        status="pending"
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment


# ➤ Get all appointments
@router.get("/", response_model=list[AppointmentResponse])
def get_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()


# ➤ Get appointment by ID
@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: UUID, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return appointment


# ➤ Update status
@router.put("/{appointment_id}")
def update_status(appointment_id: UUID, status: str, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointment.status = status
    db.commit()
    return {"message": "Status updated"}
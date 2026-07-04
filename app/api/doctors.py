from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.database import get_db
from app.models.doctors import Doctor
from app.schemas.doctor import DoctorCreate, DoctorResponse

router = APIRouter(prefix="/doctors", tags=["Doctors"])


# ➤ Create Doctor
@router.post("/", response_model=DoctorResponse)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    new_doctor = Doctor(**doctor.dict())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor


# ➤ Get all doctors
@router.get("/", response_model=list[DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()


# ➤ Get doctor by ID
@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: UUID, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


# ➤ Update doctor
@router.put("/{doctor_id}", response_model=DoctorResponse)
def update_doctor(doctor_id: UUID, updated: DoctorCreate, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    for key, value in updated.dict().items():
        setattr(doctor, key, value)

    db.commit()
    db.refresh(doctor)
    return doctor


# ➤ Delete doctor
@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: UUID, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    db.delete(doctor)
    db.commit()
    return {"message": "Doctor deleted successfully"}
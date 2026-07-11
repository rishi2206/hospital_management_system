from fastapi import FastAPI

from app.api import auth
from app.api import users
from app.api import patients
from app.api import medicine
from app.api import prescriptions
from app.api import bill
from app.api.doctors import router as doctor_router
from app.api.appointments import router as appointment_router
from app.api.departments import router as department_router
from app.models.users import Users
from app.models.roles import Role
from app.models.patients import Patient
from app.models.doctors import Doctor
from app.models.medical_history import Medical_history
from app.models.appointments import Appointment
from app.models.prescriptions import Prescription
from app.models.bill import Bill

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(patients.router)
app.include_router(doctor_router)
app.include_router(appointment_router)
app.include_router(department_router)
app.include_router(medicine.router)
app.include_router(prescriptions.router)
app.include_router(bill.router)
from fastapi import FastAPI
from app.api import auth, users, patients

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(patients.router)
from app.api.doctors import router as doctor_router
app.include_router(doctor_router)
from app.api.appointments import router as appointment_router
app.include_router(appointment_router)
from app.api.departments import router as department_router
app.include_router(department_router)
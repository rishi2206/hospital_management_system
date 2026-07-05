from fastapi import FastAPI
<<<<<<< HEAD
from app.api import auth, users, patients
=======

from app.api import auth
from app.api import users
from app.api import medicine
from app.api import prescriptions
from app.api import bill
>>>>>>> 0837863 (Refactor billing, medicine, CRUD structure and add repositories/schemas)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
<<<<<<< HEAD
app.include_router(patients.router)
from app.api.doctors import router as doctor_router
app.include_router(doctor_router)
from app.api.appointments import router as appointment_router
app.include_router(appointment_router)
from app.api.departments import router as department_router
app.include_router(department_router)
=======
app.include_router(medicine.router)
app.include_router(prescriptions.router)
app.include_router(bill.router)
>>>>>>> 0837863 (Refactor billing, medicine, CRUD structure and add repositories/schemas)

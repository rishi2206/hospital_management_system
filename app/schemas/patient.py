from pydantic import BaseModel, EmailStr
from uuid import UUID


class PatientCreate(BaseModel):
    user_id: UUID
    name: str
    Gender: str
    Age: int
    Phone_number: str
    email: EmailStr
    blood_group: str | None = None
    emergency_contact: str | None = None


class PatientUpdate(BaseModel):
    name: str | None = None
    Gender: str | None = None
    Age: int | None = None
    Phone_number: str | None = None
    email: EmailStr | None = None
    blood_group: str | None = None
    emergency_contact: str | None = None


class PatientResponse(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    Gender: str
    Age: int
    Phone_number: str
    email: EmailStr
    blood_group: str | None = None
    emergency_contact: str | None = None

    class Config:
        from_attributes = True
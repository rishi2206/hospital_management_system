from pydantic import BaseModel,EmailStr
from uuid import UUID

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role_id: UUID
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    role_id: UUID | None = None
    
class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    role_id: UUID
    
    class Config:
        from_attributes = True
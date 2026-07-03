from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate,UserLogin,UserResponse
from app.services import auth_service

router = APIRouter(
    prefix="/auth",
    tags =["Authentication"]
)

@router.post(
    "/register",
    response_model=UserResponse
)
def register(user: UserCreate, db: Session=Depends(get_db)):
    try:
        return auth_service.register_user(db,user)
    except ValueError as e:
        raise HTTPException(status_code=400 , detail=str(e))
    
@router.post("/login")

def login(login_data: UserLogin , db: Session = Depends(get_db)):
    try:
        return auth_service.login_user(db,login_data)
    except ValueError as e:
        raise HTTPException(status_code=401,detail=str(e))
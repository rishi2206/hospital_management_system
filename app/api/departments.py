from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.database import get_db
from app.models.departments import Department
from app.schemas.department import DepartmentCreate, DepartmentResponse

router = APIRouter(prefix="/departments", tags=["Departments"])


# ➤ Create Department
@router.post("/", response_model=DepartmentResponse)
def create_department(data: DepartmentCreate, db: Session = Depends(get_db)):
    new_dept = Department(**data.dict())
    db.add(new_dept)
    db.commit()
    db.refresh(new_dept)
    return new_dept


# ➤ Get all departments
@router.get("/", response_model=list[DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):
    return db.query(Department).all()


# ➤ Get by ID
@router.get("/{dept_id}", response_model=DepartmentResponse)
def get_department(dept_id: UUID, db: Session = Depends(get_db)):
    dept = db.query(Department).filter(Department.id == dept_id).first()

    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")

    return dept


# ➤ Delete department
@router.delete("/{dept_id}")
def delete_department(dept_id: UUID, db: Session = Depends(get_db)):
    dept = db.query(Department).filter(Department.id == dept_id).first()

    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")

    db.delete(dept)
    db.commit()

    return {"message": "Department deleted"}
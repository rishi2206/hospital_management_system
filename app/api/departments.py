from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.department import DepartmentCreate, DepartmentResponse
from app.services import department_service

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


# Create Department
@router.post("/", response_model=DepartmentResponse)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    return department_service.create_department(db, department)


# Get all Departments
@router.get("/", response_model=list[DepartmentResponse])
def get_departments(
    db: Session = Depends(get_db)
):
    return department_service.get_all_departments(db)


# Get Department by ID
@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department(
    department_id: UUID,
    db: Session = Depends(get_db)
):
    department = department_service.get_department_by_id(db, department_id)

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    return department


# Update Department
@router.put("/{department_id}", response_model=DepartmentResponse)
def update_department(
    department_id: UUID,
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    existing_department = department_service.get_department_by_id(db, department_id)

    if not existing_department:
        raise HTTPException(status_code=404, detail="Department not found")

    existing_department.name = department.name
    existing_department.description = department.description

    return department_service.update_department(db, existing_department)


# Delete Department
@router.delete("/{department_id}")
def delete_department(
    department_id: UUID,
    db: Session = Depends(get_db)
):
    department = department_service.get_department_by_id(db, department_id)

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    department_service.delete_department(db, department)

    return {"message": "Department deleted successfully"}
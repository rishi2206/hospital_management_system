import uuid
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from app.database import Base

class Medicine(Base):
    __tablename__ = "medicine"
    
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    medicine_name = Column(String(100), nullable=False)
    stock = Column(Integer,nullable=False)
    expiry_date = Column(Date, nullable=False)
    manufacture = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
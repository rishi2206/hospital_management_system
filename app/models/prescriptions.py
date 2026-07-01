import uuid
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from app.database import Base

class Prescription(Base):
    __tablename__ = "prescriptions"
    
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    medical_history_id = Column()
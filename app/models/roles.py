from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class Role(Base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, nullable=False,index=True)
    name = Column(string, unique=true , nullable=False)
    description = Column(Text,nullable=True)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    updated_at = Column(
        DataTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    
    
    users = relationship("Users",back_populates="role")
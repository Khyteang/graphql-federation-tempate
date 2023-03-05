from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from db_conf import Base

class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gender = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), server_default=func.now())
    
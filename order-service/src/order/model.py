from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from db_conf import Base

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), server_default=func.now())

    patient_id = Column(Integer)
    prescription_id = Column(Integer)
    status = Column(String)

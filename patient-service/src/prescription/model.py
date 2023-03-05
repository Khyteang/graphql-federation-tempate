from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db_conf import Base

class Prescription(Base):
    __tablename__ = "prescription"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    med_id = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), server_default=func.now())

    patient_id = Column(
        Integer,
        ForeignKey('patient.id', ondelete='CASCADE'),
        nullable=False,
    )
    patient = relationship('Patient', backref='prescriptions')
import typing

from db_conf import db_session
from src.prescription.model import Prescription

db = db_session.session_factory()

async def get_prescriptions() -> typing.List[Prescription]:
    return db.query(Prescription).all()

async def add_prescription(patient_id, name, med_id) -> Prescription:
    new_prescription = Prescription(
      name=name,
      med_id=med_id,
      patient_id=patient_id
    )
    db.add(new_prescription)
    db.commit()
    db.refresh(new_prescription)
    return new_prescription    
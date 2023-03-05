import typing
from db_conf import db_session
from src.patient.model import Patient

db = db_session.session_factory()

async def get_patients() -> typing.List[Patient]:
    result = db.query(Patient).all()
    return result

async def get_patient_by_id(patient_id) -> Patient:
    result = db.query(Patient).filter(Patient.id == patient_id).first()
    return result

async def add_patient(name, gender) -> Patient:
    new_patient = Patient(
      name=name,
      gender=gender
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

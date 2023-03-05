import typing
import strawberry
import src.patient.service as service
from src.prescription.schema import Prescription

@strawberry.federation.type(keys=["id"])
class Patient:
    id: strawberry.ID
    name: str
    gender: str
    prescriptions: typing.List[Prescription]

@strawberry.type
class Query:
    patients: typing.List[Patient] = strawberry.field(resolver=service.get_patients)
    @strawberry.field
    def get_patient_by_id(self, info, patient_id: str = None) -> Patient:
        return service.get_patient_by_id(patient_id)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_patient(self, name: str, gender: str) -> Patient:
        return service.add_patient(name, gender)
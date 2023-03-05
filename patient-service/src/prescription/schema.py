import typing
import strawberry

import src.prescription.service as service

@strawberry.type
class Prescription:
    id: int
    name: str
    med_id: str

@strawberry.type
class Query:
    prescriptions: typing.List[Prescription] = strawberry.field(resolver=service.get_prescriptions)    

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_prescription(self, patient_id: str, name: str, med_id: str) -> Prescription:
        return service.add_prescription(patient_id, name, med_id)
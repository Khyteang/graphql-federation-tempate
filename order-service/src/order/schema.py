import typing
import strawberry
import src.order.service as service

@strawberry.type
class Order:
    id: int
    patient_id: int
    prescription_id: int
    status: str

def get_orders(root) -> typing.List[Order]:
    print(f"root: {root}")
    return service.get_orders()

@strawberry.federation.type(keys=["id"])
class Patient:
    id: strawberry.ID
    orders_count: int
    orders: typing.List[Order] = strawberry.field(resolver=get_orders)

    @classmethod
    def resolve_reference(self, id: strawberry.ID):
        return Patient(id=id, orders_count=1)

@strawberry.type
class Query:
    orders: typing.List[Order] = strawberry.field(resolver=service.get_orders)
    @strawberry.field
    def get_orders_by_patient_id(self, info, patient_id: int) -> typing.List[Order]:
        return service.get_orders_by_patient_id(patient_id=patient_id)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_order(self, patient_id: int, prescription_id: int) -> Order:
        return service.create_order(patient_id, prescription_id)

import typing
from src.order.model import Order
from db_conf import db_session

db = db_session.session_factory()

async def create_order(patient_id: int, prescription_id: int) -> Order:
    new_order = Order(
        patient_id=patient_id,
        prescription_id=prescription_id,
        status="CREATED"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

async def get_orders_by_patient_id(patient_id: int) -> typing.List[Order]:
    result = db.query(Order).filter(Order.patient_id == patient_id).all()
    return result

async def get_orders() -> typing.List[Order]:
    result = db.query(Order).all()
    return result
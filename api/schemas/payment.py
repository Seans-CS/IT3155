from typing import Optional
from pydantic import BaseModel

from api.schemas.orders import OrderBase


class PaymentBase(BaseModel):
    card_info: Optional[str]
    transaction_status: Optional[str]
    payment_type: Optional[str]
    order_id: Optional[int]


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    card_info: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None
    order_id: Optional[int] = None


class Payment(PaymentBase):
    id: int
    order: Optional[OrderBase]

    class Config:
        orm_mode = True

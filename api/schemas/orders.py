from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .customer import Customer
from .payment import Payment
from .restaurant import Restaurant


class OrderBase(BaseModel):
    order_date: Optional[datetime]
    tracking_number: Optional[str]
    order_status: Optional[str]
    total_price: Optional[float]
    customer_email: Optional[str]
    payment_id: Optional[int]
    order_details: Optional[str]
    restaurant_id: Optional[int]


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    order_date: Optional[datetime] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None
    customer_email: Optional[str] = None
    payment_id: Optional[int] = None
    order_details: Optional[str] = None
    restaurant_id: Optional[int] = None


class Order(OrderBase):
    id: int
    customer: Optional[Customer]
    payment: Optional[Payment]
    restaurant: Optional[Restaurant]

    class Config:
        orm_mode = True

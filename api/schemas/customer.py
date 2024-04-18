from datetime import datetime
from typing import Optional
from pydantic import BaseModel
# from .orders import Order


class CustomerBase(BaseModel):
    name: str
    address: str
    phone_number: str


class CustomerCreate(CustomerBase):
    order_details: Optional[int] = None


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
#     order_details: Optional[Order] = None


class Customer(CustomerBase):
    email: str
    # order: Order = None

    class ConfigDict:
        from_attributes = True

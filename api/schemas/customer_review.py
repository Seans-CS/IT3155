from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .customer import Customer


class Customer_ReviewBase(BaseModel):
    review: str
    score: str
    


class Customer_ReviewCreate(Customer_ReviewBase):
    customer: Optional[Customer] = None


class Customer_ReviewUpdate(BaseModel):
    review: Optional[str] = None
    score: Optional[int] = None



class Customer_Review(Customer_ReviewBase):
    customer: Customer = None

    class ConfigDict:
        from_attributes = True

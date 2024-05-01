from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class RestaurantBase(BaseModel):
    name: str
    Menu: str
    Promotions: str


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantUpdate(BaseModel):
    restaurant_name: Optional[str] = None
    Menu: Optional[str] = None


class Restaurant(RestaurantBase):
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True

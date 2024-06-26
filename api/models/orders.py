from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
# from .models.customer import Customer
# from .models.restaurant import Restaurant


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(Date, nullable=False, server_default=str(datetime.now()))
    tracking_number = Column(String(100))
    order_status = Column(String(100))
    total_price = Column(Float)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="order")
    payment_id = Column(Integer, ForeignKey("payments.id"))
    payment = relationship("Payment", back_populates="order")
    order_details = Column(String(300))
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    restaurant = relationship("Restaurant", back_populates="orders")

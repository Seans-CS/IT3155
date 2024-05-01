from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base



class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(Date, nullable=False, server_default=str(datetime.now()))
    tracking_number = Column(String(100))
    order_status = Column(String(100))
    total_price = Column(Float)
    customer_email = Column(String(100), ForeignKey("Customer.email"))
    customer = relationship("Customer", back_populates="orders")
    payment_id = Column(Integer, ForeignKey("payments.id"))
    payment = relationship("Payment", back_populates="order")
    order_details = Column(String(300))
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    restaurant = relationship("Restaurant", back_populates="orders")

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = 'Customer'

    name = Column(String(100), nullable=False, index=True)
    email = Column(String(100), primary_key=True, index=True)
    phoneNumber = Column(String(100), nullable=False, index=True)
    address = Column(String(100), nullable=False, index=True)
    order_details_id = Column(Integer, ForeignKey("order_details.id"))
    orderDetails = relationship("Order_details", back_populates="customer")

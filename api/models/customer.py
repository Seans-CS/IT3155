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
    orders_id = Column(Integer, ForeignKey("Orders.id"))
    order = relationship("Orders", back_populates="customer")

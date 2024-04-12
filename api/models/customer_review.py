from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
# from . import customer
from ..dependencies.database import Base


class CustomerReview(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review = Column(String(1000), nullable=False, index=True)
    score = Column(Integer, nullable=False, index=True)
    # customer = Column(customer.Customer, nullable=False, index=True)
    customer = relationship("Customer", back_populates="customer_review")

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from .orders import Order


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_info = Column(String(100))
    transaction_status = Column(String(100))
    payment_type = Column(String(100))
    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship("Order", back_populates="payment")

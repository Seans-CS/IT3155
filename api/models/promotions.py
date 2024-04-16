
from sqlalchemy import Column, Integer, String, DateTime
from ..dependencies.database import Base
from datetime import datetime

class Promotion(Base):
    __tablename__ = 'promotions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime)

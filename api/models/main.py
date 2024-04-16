from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON  # Assuming using PostgreSQL

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'Restaurant'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    # Storing JSON data in the menu and promotions columns
    menu = Column(JSON, nullable=True)
    promotions = Column(JSON, nullable=True)

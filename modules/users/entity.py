from sqlalchemy import Column, Integer, String, DateTime
from core.database import Base
from datetime import datetime
from typing import Generic, TypeVar

T = TypeVar('T')

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone_number = Column(String)

    first_name = Column(String)
    last_name = Column(String)

    create_date = Column(DateTime, default=datetime.now())
    update_date = Column(DateTime)

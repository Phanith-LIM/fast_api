from sqlalchemy import Column, String, DateTime, UUID
from core import Base
from datetime import datetime
from typing import TypeVar
import uuid

T = TypeVar('T')

class Users(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True, unique=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone_number = Column(String)

    first_name = Column(String)
    last_name = Column(String)

    create_date = Column(DateTime, default=datetime.now())
    update_date = Column(DateTime)



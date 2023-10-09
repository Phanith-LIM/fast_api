import uuid
from core import Base
from typing import TypeVar
from .model import UserModel
from datetime import datetime
from passlib.context import CryptContext
from sqlalchemy import Column, String, DateTime, UUID

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

    @staticmethod
    def from_model(model: UserModel):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return Users(
            username=model.username,
            email=model.email,
            phone_number=model.phone_number,
            password=pwd_context.hash(model.password),
            first_name=model.first_name,
            last_name=model.last_name
        )

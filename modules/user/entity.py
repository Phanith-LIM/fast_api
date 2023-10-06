from sqlalchemy import Column, Integer, String

from core.database import Base

class User(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    age = Column(Integer)
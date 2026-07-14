# pyrefly: ignore [missing-import]
from pandas.core import indexing
from sqlalchemy import Column, Integer, String
from database.database import Base

class RegisteredUsers(Base):
    __tablename__ = "registered_users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, index=True)
    phone_number = Column(String, index=True)
    
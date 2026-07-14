from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base

class RegisteredUsers(Base):
    __tablename__ = "registered_users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    is_active = Column(Boolean, default=True)

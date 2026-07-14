from database.database import Base
# pyrefly: ignore [missing-import]
from sqlalchemy import Column, String, Integer, Float

class PolicyDetails(Base):
    __tablename__ = "policy_details"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name=Column(String, index=True)
    policy_id=Column(Integer, index=True)
    policy_type = Column(String, index=True)
    policy_amount = Column(Float, index=True)
    renewal_date = Column(String, index=True)
    expiry_date = Column(String, index=True)
    date_of_purchase=Column(String, index=True)
    
    

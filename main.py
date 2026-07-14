from database.database import Base, engine
from fastapi import FastAPI
from api.healthcheck import router as healthcheck_router
from api.login import router as login_router
# Import models
from models.registered_users import RegisteredUsers
from models.policy_details import PolicyDetails

# Create all tables
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")


app = FastAPI()
app.include_router(healthcheck_router)
app.include_router(login_router)

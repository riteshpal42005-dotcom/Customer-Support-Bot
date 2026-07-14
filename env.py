import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print("DATABASE_URL =", DATABASE_URL)

ADMIN_NAME = os.getenv("ADMIN_NAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(".env")

api_key = os.getenv("API_KEY")
db_url = os.getenv("DATABASE_URL")

print("API_KEY:", api_key)
print("DATABASE_URL:", db_url)

# DO NOT hard-code secrets like this:
# api_key = "supersecret123"

import os
from dotenv import load_dotenv

load_dotenv()

profile={
    "name": "Sania",
    "niche": "Tech specifically AI and Python",
    "tone": "Professional and impressive",
    "post_time": "13:54",
    "language":"English"
}

BUFFER_API_KEY = os.getenv("BUFFER_API_KEY")
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
CHANNEL_ID = os.getenv("CHANNEL_ID")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

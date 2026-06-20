import os
from dotenv import load_dotenv

load_dotenv()

profile={
    "name": "Sania",
    "niche": "Tech specifically AI and Python",
    "tone": "Professional and impressive",
    "post_time": "13:30",
    "language":"English"
}

BUFFER_API_KEY = os.getenv("BUFFER_API_KEY")

CHANNEL_ID = os.getenv("CHANNEL_ID")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

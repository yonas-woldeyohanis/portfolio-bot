# config.py
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_USER_ID = os.getenv("ADMIN_USER_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") # <--- ADD THIS




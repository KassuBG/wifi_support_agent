# Description: File contains the configuration settings for the application.
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG", "False") == "True"
    PORT = int(os.getenv("PORT", 8000))
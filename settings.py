from dotenv import load_dotenv
from pathlib import Path
import os

EnvPath = Path('.') / '.env'
load_dotenv(dotenv_path=EnvPath)

class Config:
    """
    Set Flask configuration vars from .env file.
    """

    # Load in enviornemnt variables
    TESTING = os.getenv('TESTING')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SERVER = os.getenv('SERVER')
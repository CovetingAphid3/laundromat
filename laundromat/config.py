from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')  # Correctly using os.getenv
    # SQLALCHEMY_DATABASE_URI = os.getenv('DB_CONNECTION_STRING') + '&ssl_ca=%2Fetc%2Fssl%2Fcert.pem'  # Use parentheses
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Replace this with your actual connection string if needed

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('EMAIL_USER')  # Correctly using os.getenv
    MAIL_PASSWORD = os.getenv('EMAIL_PASS')  # Correctly using os.getenv


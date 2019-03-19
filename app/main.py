from flask import Flask
from app.utils.config import DevelopmentConfig

def configure_app():
    app = Flask(__name__)
    app.secret_key = DevelopmentConfig.SECRET_KEY
    return app

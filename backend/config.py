"""Flask configuration."""
import os

class Config:
    """Base config."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    APIFAIRY_TITLE = 'Preqin Backend API'
    APIFAIRY_VERSION = os.environ.get('APIFAIRY_VERSION')
    APIFAIRY_UI_PATH = '/api/docs'
    APIFAIRY_UI = 'swagger_ui'

class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class LocalConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #SQLite database for development
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite')}"

class TestConfig(Config):
    TESTING = True
import os
import re

class Config:
    """
    General configuration parent class
    """
    # Data base config
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://obafemi:Bentamjay1@localhost/pitches'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

class ProdConfig(Config):
    """
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """

    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = uri


class DevConfig(Config):
    """
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://obafemi:Bentamjay1@localhost/pitches'

    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://obafemi:Bentamjay1@localhost/pitches_test'

config_options = {"development": DevConfig, "production": ProdConfig, 'test':TestConfig}

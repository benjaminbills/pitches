import os


class Config:
    """
    General configuration parent class
    """
    # Data base config
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://obafemi:Bentamjay1@localhost/pitches'



class ProdConfig(Config):
    """
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """

    pass


class DevConfig(Config):
    """
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://obafemi:Bentamjay1@localhost/pitches'

    DEBUG = True

class TestConfig(Config):
    pass

config_options = {"development": DevConfig, "production": ProdConfig, 'test':TestConfig}

import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2015@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Blog'
    SENDER_EMAIL = 'cherotichm23@gmail.com'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod 
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2015@localhost/blogs'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    SQLALCHEMY_DATABASE_URI  ='postgresql://jwwgorxkpqcxle:434f94ccb778a0d6bf62316163b80a4daaf1a133e593d700ba47701e38d7d140@ec2-34-231-183-74.compute-1.amazonaws.com:5432/dbqdjqpuk0bapa'



class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2015@localhost/blogs_test'
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2015@localhost/blogs'
    DEBUG = True


 
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}
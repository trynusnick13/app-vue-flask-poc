import os


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:testing@localhost/postgres"
    APP_DIR = os.path.dirname(__file__)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = os.environ
    # SECRET_KEY = 'very secret key'

    ### Flask-security ###
    # SECURITY_PASSWORD_SALT = 'salt'
    # SECURITY_PASSWORD_HASH = 'bcrypt'
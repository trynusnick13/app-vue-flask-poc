import os


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:testing@localhost/postgres"
    SQLALCHEMY_DATABASE_URI = "postgresql://vbfbvasilnfmdk:546a5d29343ddf6c01ac0032ad5aecda9568d7cd0e6b68d10e0f9ff15f7871c1@ec2-18-214-195-34.compute-1.amazonaws.com:5432/d34a854l5lrfq7"
    APP_DIR = os.path.dirname(__file__)
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = os.environ
    # SECRET_KEY = 'very secret key'

    ### Flask-security ###
    # SECURITY_PASSWORD_SALT = 'salt'
    # SECURITY_PASSWORD_HASH = 'bcrypt'
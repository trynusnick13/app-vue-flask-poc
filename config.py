class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:testing@localhost/postgres"
    # SECRET_KEY = 'very secret key'

    ### Flask-security ###
    # SECURITY_PASSWORD_SALT = 'salt'
    # SECURITY_PASSWORD_HASH = 'bcrypt'
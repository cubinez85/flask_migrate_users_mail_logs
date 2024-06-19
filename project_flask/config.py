import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'qwerty'

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://cubinez85:123@localhost/testdb'

    


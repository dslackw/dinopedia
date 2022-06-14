import os

# URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/dinopedia'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    SECRET_KEY = 'mysecretkey'

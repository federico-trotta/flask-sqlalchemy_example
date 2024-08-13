import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskuser:your_password@localhost/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

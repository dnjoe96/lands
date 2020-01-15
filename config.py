import os
# install dotenv and python-dotenv
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


# creating a configuration class
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default'
    # 'mssql+pyodbc://<username>:<password>@<Host>:<Port>/LendApp'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # to disable the feature of flask SQAlchemy that signals application each time a change is made

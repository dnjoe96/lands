from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)
moment = Moment(app)
db = SQLAlchemy(app)

from sqlalchemy import create_engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
connection = engine.connect()

from app import routes


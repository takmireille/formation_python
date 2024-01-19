# my_models/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

my_App = Flask(__name__)
my_App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.sqlite'
db = SQLAlchemy()
db.init_app(my_App)

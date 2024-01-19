# my_models.py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.sqlite'
db = SQLAlchemy()
db.init_app(app)

class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    level = db.Column(db.Integer, nullable=False)
    date_last_test = db.Column(db.Date, nullable=True)

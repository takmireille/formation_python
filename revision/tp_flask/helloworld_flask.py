
from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")

def hello_word():
    return "hello word!"

@app.route("/python")

def python():
    return " Le python, c'est la vie!"

@app.route("/homepage")

def homepage():
    apps = [ { "name": "papa", "level": 2},
            {"name": "Cyrille", "level": 7},
            { "name": "Rene", "level": 8}   ]
    return render_template('hello.html',
                           name="sacha",
                           apps=apps)
   
    
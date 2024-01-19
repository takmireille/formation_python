
from flask import Flask, render_template
from my_models import my_app  

app = Flask(__name__)

@app.route("/")
def homepage():
    apps = [
        {"name": "papa", "level": 2},
        {"name": "Cyrille", "level": 7},
        {"name": "Rene", "level": 8}
    ]
    return render_template('hello.html', 
                           name="Mireille", 
                           apps=apps)




from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    apps = [
        {"name": "papa", "level": 2},
        {"name": "Cyrille", "level": 7},
        {"name": "Rene", "level": 8}
    ]
    return render_template('hello.html', name="Mireille", apps=apps)

    

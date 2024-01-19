from flask import render_template
from my_models import app

@app.route('/')
def homepage():
    apps = app.query.all()
    return render_template('hello.html'
                           prenom="Mireille",
                           apps=apps)
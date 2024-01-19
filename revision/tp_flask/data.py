from flask import render_template
from flask import Flask
from my_models import App # Assurez-vous que vous importez la classe correcte
app = Flask(__name__)

@app.route("/")
def homepage():
    apps = App.query.all()
    return render_template('hello.html',
                           prenom="Mireille",
                           apps=apps)


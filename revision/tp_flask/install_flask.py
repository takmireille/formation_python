
import os

def install_flask():

    try:
        #l'installation de l'environnment flask
        os.system("pip install flask")
        os.system("pip install flask-SQLAIchemy")
        #print("environnement flask installer avec susccès")
    except Exception as:
        print(" une erreur c'est produite")

# execution
install_flask()
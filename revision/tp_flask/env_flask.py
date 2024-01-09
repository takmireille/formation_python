# ce script permet l'installation de l'environnement virtuel pour flask

import os 
import sys

def installation_env():

    try:
        os.system("apt install python3-virtualenv virtualenv") # installation de l'environnement virtuel (root)
        os.system("virtualenv -ppython3 venv")
        os.system("source venv/bin/activate") # activer l'environnement virtuel
        
        #einstallation de l'environnment flask
        os.system("pip install flask")
        os.system("pip install flask-SQLAIchemy")
        print("environnement flask installer avec susccès")
    except Exception as e:
        print("une erreur s'est produite lors de la configuration de l'environnement virtuel")
        sys.exit(1)
# execution

installation_env()

    
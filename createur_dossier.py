# Le but de ce projet est donc de créer une structure de dossiers à partir d'un dictionnaire.
from pathlib import Path
# on specifie le chemin pour l'emplacement des dossiers et sous dossiers

chemin = Path("/home/tak/Documents/dossier_test")

# creation des dossiers et sous dossiers

doc = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

for dossier_principal, sous_dossiers in doc.items():
    for dossier in sous_dossiers:
        chemin_dossier = Path(chemin) / dossier_principal / dossier
        chemin_dossier.mkdir(exist_ok=True, parents=True)


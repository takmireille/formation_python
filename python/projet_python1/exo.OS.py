import os
# definition des actions possibles
# ici on considre le cas ou les actions sont faites dans la norme si le dossier n'existe pas
def créer_dossier(chemin):
  try:
    os.mkdir(chemin)
    print("dossier créer")
  except:
    print("le dossier existe deja")

def suprimer_dossier(chemin):
  try:
    os.rmdir(chemin)
    print("dossier suprimer")
  except:
    print("le dossier existe deja")
def verification_existance(chemin):
  if os.path.exists(chemin):
    print("le  dossier existe")
  else:
    print("le dossier n'existe pas")
# condition 
while True:
  print("action possibles:\n1- creer un dossier\n2- suprimer un dossier\n3- verifier l'existance d'un dossier")
choix = input("choisissez une action parmi les 3 prposées :"  )
  if choix == "1":
     chemin = input("Entrez le chemin du dossier:  ")
     créer_dossier(chemin)
  elif choix == "2":
    chemin = input("Entrez le chemin du dossier à suprimer:  ")
    suprimer_dossier(chemin)
  elif choix == "3":
    chemin = input("Entrez le chemin du dossier à verifier:  ")
    verification_existance(chemin) 
    break

import os
# action à mener


def menu():
  print("Vous pouvez travailler dans un dossier ou sur un fichier.")
  print("1 - Dossier")
  print("2 - Fichier")
  choix_menu = input("Entrez votre choix : ")
  return choix_menu


def actions_dossier():
  print("Les tâches possibles sont :")
  print("1 - Créer un dossier")
  print("2 - Lister le contenu d'un dossier")
  print("3 - Renommer le dossier")
  print("4 - Supprimer le dossier")
  choix_actionD = input("Entrez votre choix : ")
  return choix_actionD


def actions_fichier():
  print("Les tâches possibles sont :")
  print("1 - Créer un fichier")
  print("2 - Vérifier si un fichier existe")
  print("3 - Renommer le fichier")
  print("4 - Supprimer le fichier")
  choix_actionF = input("Entrez votre choix : ")
  return choix_actionF


def creer_dossier():
  nom_dossier = input("Entrez le nom du dossier : ")
  try:
    os.makedirs(nom_dossier)
    print("Le dossier a été créé.")
  except:
    print("Le nom_dossier existe déjà.")
    


def lister_contenu_dossier():
  nom_dossier = input("Entrez le nom du dossier : ")
  contenu = os.listdir(nom_dossier)
  print("Contenu du dossier :")
  for element in contenu:
    print(element)


def renommer_dossier():
  ancien_nom = input("Entrez l'ancien nom du dossier : ")
  nouveau_nom = input("Entrez le nouveau nom du dossier : ")
  try:
    os.rename(ancien_nom, nouveau_nom)
    print("Le dossier a été renommé.")
  except:
    print("Le dossier n'existe pas.")


def supprimer_dossier():
  nom_dossier = input("Entrez le nom du dossier : ")
  try:
    os.rmdir(nom_dossier)
    print("Le dossier a été supprimé.")
  except:
    print("Le dossier n'existe pas.")


def creer_fichier():
  nom_fichier = input("Entrez le nom du fichier : ")
  try:
    with open(nom_fichier, 'x') as fichier:
      print("Le fichier a été créé.")
  except:
    print("Le fichier existe déjà.")


def verifier_fichier():
  nom_fichier = input("Entrez le nom du fichier : ")
  if os.path.exists(nom_fichier):
    print("Le fichier existe.")
  else:
    print("Le fichier n'existe pas.")


def renommer_fichier():
  ancien_nom = input("Entrez l'ancien nom du fichier : ")
  nouveau_nom = input("Entrez le nouveau nom du fichier : ")
  try:
    os.rename(ancien_nom, nouveau_nom)
    print("Le fichier a été renommé.")
  except:
    print("Le fichier n'existe pas.")


def supprimer_fichier():
  nom_fichier = input("Entrez le nom du fichier : ")
  try:
    os.remove(nom_fichier)
    print("Le fichier a été supprimé.")
  except:
    print("Le fichier n'existe pas.")


# Phase interactive
choix_menu = menu()

if choix_menu == "1":
  # Routines Dossiers
  choix_actionD = actions_dossier()

  if choix_actionD == "1":
    creer_dossier()
  elif choix_actionD == "2":
    lister_contenu_dossier()
  elif choix_actionD == "3":
    renommer_dossier()
  elif choix_actionD == "4":
    supprimer_dossier()

elif choix_menu == "2":
  # Routines Fichiers
  choix_actionF = actions_fichier()

  if choix_actionF == "1":
    creer_fichier()
  elif choix_actionF == "2":
    verifier_fichier()
  elif choix_actionF == "3":
    renommer_fichier()
  elif choix_actionF == "4":
    supprimer_fichier()




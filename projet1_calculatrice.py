#creation d'une calculatrice en ligne pour additionner deux nombres
# 1- recuperer la saisie de l'utilisateur
# 2- afficher le resultat

nombre1 = input ("veuillez entrer un premier nombre :")

nombre2 = input ("veuillez entrer le deuxieme nombre :")


resultat = {int(nombre1) + int(nombre2)}


print (f"le résultat de la somme {nombre1} avec {nombre2} est égal à {int(nombre1) + int(nombre2)}")

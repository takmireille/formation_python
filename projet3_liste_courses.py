# liste des courses : le but n'est pas de sauvegerder al liste , mais d'interagir avec l'utilisateur

liste = [ ]

menu = input("""veuille choisir une option parmi les suivantes:
1:Ajouter les élements à la liste
2:Retirer un élément à la liste
3:Afficher les éléments de la liste
4:Vider la liste
5:quitter
?votre choix :""")

if int(menu) == int(0):
	print ("veuillez entrer choisir une option valide")
if int(menu) > int(5):

	print ("veuillez entrer choisir une option valide")

if int(menu) == int(1):

	element = input("donner le nom l'élement à ajouter")
	
	liste.append(element)

	print (f"l'élement {element} a été ajouté")
if int(menu) == int(2):

	element_suprime = input("donnez le nom de l'élément à suprimer:")

	if element_suprime in liste:

		liste.remove(element_suprime)
	
		print (f"l'element {element_suprime} a été retiré")
	elif element_suprime not in liste:

		print (f"l'élément {element_suprime} n'est pas dans la liste")

if int(menu) == int(3):

	for i, element in enumerate(liste):

        	print (i, element)
	


if int(menu) ==  int(4):

	liste.clear()
	print ("la liste a été vidée")

elif int(menu) == int(5):

	print ("liste terminée.A bientot")
	







# sortir d'une boucle infinie

#i = 0

#while i < 10:
#	pass
	
#resultat = "Exercice réussi !"

# script corrigé

i = 0

while i < 10:

	i+=1
resultat = "Execice réussi!"

print(resultat)

# Sortir d'une boucle while avec input

continuer = input("voulez-vous continuez? o/n")


while continuer == "o":

	print ("On continue")
	continuer = input("voulez-vous continuez? o/n")
	
	if continuer == "n":

		print ("stop")




# anticiper les erreurs au cas ou l'utlisateur n'entre pas les deux nombres dans la calculatrice, pour que le script ne  produise pas d'erreur 

print ("Bonjour!")
a = input("Entrez un premier nombre :")

b = input("Entrez un deuxieme nombre:")

if (a.isdigit() == True and b.isdigit() == True):

	print(f"les deux nombres sont valides: le resultat de {a} +{b} est {int(a) + int(b) }")

if not (a.isdigit() and b.isdigit()):

	print("veuillez entrez deux nombres valides")


# afficher avec une boucle les dix utilisateurs

print("1-Afficher avec une boucle les dix utilisateurs")


for i in range(10):

	print(f"utilisateur{i + 1}")

# afficher un mot à l'envers
print("2- Afficher le mot amour à l'envers")

mot = "amour"

print ("".join(reversed(mot)))

# fixer l'érreur dans la boucle: le but est de modifier le script afin d'afficher l'index de chaque lettre du mot "python"

#mot = "Python"

#for i in range(mot):
#    print(i)

#script modifié
print("2-Afficher les index des lettres du mot python")
mot = "python"

for i in range(len(mot)):
	print(i)
# afficher la table de multilication du nombre 7

print ("3- afficher la table de multiplication du nombre 7")

for i in range(11):

	print (f"{i} x {7} = {i * 7}")

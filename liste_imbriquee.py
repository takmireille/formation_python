# recuperer les éléments dans une liste imbriquée
print ("soient les listes languages et nombres")

languages = [["Python","C++"], "Java"]

nombres = [1, [4, [2,3]], 5, [6], [[7]]]

print (languages)

print (nombres)

print("1-extraire la chaine de caractère Python de la liste languages")

python = languages[0][0]

print (python)

print ("2-recuperer les elements 2 et 7 dans la variable nombres")

deux = nombres[1][1][0]

print (deux)

sept = nombres[4][0][0]

print(sept)





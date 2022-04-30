# remplacer des boucles par des comprehensions de listes

print("1-liste des nombres pairs")

nombres = [1, 21, 5, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]

nombres_pairs = [i for i in nombres if i%2 == 0]

print (nombres_pairs)
#-----------------------------------------------------------------------------

print ("2- liste des doubles des nombres")

nombres = range(5)
doubles_nombres = [i * 2 for i in nombres]

print (doubles_nombres)
#-----------------------------------------------------------------------------
print ("3- nombres inverses")

nombres = range(10)

nombres_inverses = [i if i % 2 == 0 else 1/i for i in nombres]

print (nombres_inverses)

#-------------------------------------------------------------------------

# recuperer seulement les nombres pairs

print ("4-les nombres pairs de la liste")

nombres = range(51)

nombre_pairs = []

for i in nombres:

    if i % 2 == 0:
        nombre_pairs.append(i)
        print(nombre_pairs)


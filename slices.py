# recuperer les elements avec les slices

print ("la liste de depart est la suivante:")

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Micheal", "Eric"]

print (liste)

trois_premiers = liste[:3]

print ("les trois premiers prenoms sont:")

print(trois_premiers)

trois_derniers = liste[3:]

print("les trois derniers prenoms sont:")

print(trois_derniers)

milieu = liste[1:-1]

print ("le mot situé au mileu est:")

print(milieu)

premier_dernier = liste[::5]

print("le premier dernier prénom de la liste est:")

print(premier_dernier)



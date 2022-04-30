#génerer deux nombres aleatoires et indiquer à l'utilisateur lequel des nombres est le plus grand




import random

nombre1 = random.randint(0,2)

nombre2 = random.randint(0,3)


if nombre1 > nombre2:
	print("le nombre1 est plus grand que le nombre2")
if nombre1 < nombre2 :

	print("le nombre1 est plus petit que le nombre2")
elif nombre1 == nombre2:
    print("Le deux nombres sont égaux.")
	

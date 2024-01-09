# cette fonction prend en argument l'age et renvoie la date de naissance

import datetime


def birth_year(age):

    #current_year = datetime.now().year

    current_year = 2024


    birth_year = current_year - age

    return birth_year

# execution 

age = int(input("entrez votre age en chiffre: "))

birth_year_user = birth_year(age)

print (f"vous avez {age} ans donc vous etes nés en {birth_year(age)}")


    
    
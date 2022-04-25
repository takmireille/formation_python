# dans ce script nous allons utliser les differetes methodes python pour, comter les occurences, compter le nombre de phrases dans un texte,ordonner une chaone de caractère.

phrase = "Bonjour tout le monde."

print(phrase)

lettre_a_chercher = "o"

print ("combien de fois la lettre o apparait dans la phrase?")

resultat = phrase.lower().count(lettre_a_chercher)

print(resultat)

#compter le nombre de phrase dans un texte

texte = "Bonjour, je suis Mireille.Je suis née au Cameroun, je suis fan de la France.je suis intéressée par les métiers des secteurs environnement, et informatique."

print(texte) 

print ("combien de phrase contient ce texte?")

resultat = texte.count(".")

print (resultat)

#ordonner une chaine de caractère
print ("remettre en ordre alphabetique les prenoms present dans la chaine de caractère suivante:")

chaine = "Mireille, Pierre, Anne, Marie, Lucien"

print (chaine)

# separation des différents prénoms de la chaine

chaine_liste = chaine.split(",")

print (chaine_liste)

#trier la chaine liste

chaine_liste.sort()
print (chaine_liste)

# mettre la chaine en ordre
chaine_en_ordre = ",".join(chaine_liste)
print (chaine_en_ordre)




# verification du mot de passe

mdp = input("entrez un mot de passe (min 8 caractère) :")



if len(mdp) == 0:
	print ("MOT DE PASSE TROP COURT")
if len(mdp) >=1 and len(mdp) < 7:
	print("Mot de pass trop court")

str.isdigit(mdp)


if str.isdigit(mdp) == True:
	print ("Votre mot de passe ne contient que des nombres")

elif str.isdigit(mdp) == False and len(mdp) >= 7:
	print ("inscription terminée")


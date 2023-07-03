from random import choice

# introduction au jeu

print("Etes-vous a defiez le harard?\n Alors Bienvenu(e) dans \n CHI-FOU-MI !")

print("Voici les criteres du jeux:\nLa pierre bat les ciseaux, les ciseaux battent le papier et le papier bat la pierre")

# mode de jeu
mode = input("Choisissez le mode de jeu:\n1 pour un jour et 2 pour deux joueurs")

## le choix du joueur

choix_du_joueur = input("choisissez entre Pierre, Papier ou Ciseaux")

while choix_du_joueur not in ["Pierre", "Papier", "Ciseaux"]:
    print("Choix invalide. Veuillez choisir entre Pierre, Papier ou Ciseaux.")
    choix_du_joueur = input("Choisissez entre Pierre, Papier ou Ciseaux : ")


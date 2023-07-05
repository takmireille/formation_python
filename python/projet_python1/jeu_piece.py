# ############  jeu de la piece au mur ########
import random
#from PIL import Image
print("Bienvenu(e) au jeu de la piece contre le mur au sol ")

# def afficher_image(image_path):
    #image = Image.open(image_path)
    #image.show()
# regles du jeu
def jouer():
  nb_joueurs = int(input("entrez le nombre de joueurs : "))
  if nb_joueurs < 2:
    input("Il faut au moins deux joueurs !. Entrez un nombre de joueurs > 1 :  ")
#def pieces(): 
jouer()
j1_pieces = 5 
j2_pieces = 5


while j1_pieces > 0 and j2_pieces > 0:
  input("joueur 1 lance la piece:" )
  input("joueur 2 lance la piece: ")
  distance_1 = random.randint(0,10)  #distance du lancer du 1er joueur
  distance_2 = random.randint( 0,1)  # distance du lancer du 2ème joueur
  if (distance_1 != distance_2):
   if distance_1 < distance_2:
      print( "joueur 1 à gagné")
      j1_pieces += 1 
      j2_pieces -= 1
   else:
      print( "joueur 2 à gagné")
      j2_pieces += 1 
      j1_pieces -= 1
  else:
   print("match nul")
if j2_pieces == 0: print("le joueur 2 a perdu\n BRAVO JOUEUR 1 VOUS ETES LE GAGNANT DE LA PARTIE") 
else: 
 print("le joueur 1 a perdu\nBRAVO JOUEUR 2 VOUS ETES LE GAGNANT DE LA PARTIE")



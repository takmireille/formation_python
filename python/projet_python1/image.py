from PIL import Image, ImageDraw, ImageFont

# Créer une nouvelle image avec une taille spécifiée
largeur = 800
hauteur = 400
couleur_fond = (255, 255, 255)   Blanc
image = Image.new("RGB", (largeur, hauteur), couleur_fond)

# Charger une police de caractères
police = ImageFont.truetype("chemin/vers/la/police.ttf", taille_police)

# Créer un objet ImageDraw pour dessiner sur l'image
dessin = ImageDraw.Draw(image)

# Dessiner un texte de bienvenue centré sur l'image
texte_bienvenue = "Bienvenue dans le jeu !"
taille_texte = dessin.textsize(texte_bienvenue, font=police)
position_x = (largeur - taille_texte[0]) // 2
position_y = (hauteur - taille_texte[1]) // 2
couleur_texte = (0, 0, 0)  # Noir
dessin.text((position_x, position_y), texte_bienvenue, font=police, fill=couleur_texte)

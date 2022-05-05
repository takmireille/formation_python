# le but de ce script est de trier les fichiers selon leur type(extension) dabs des sous dossiers.

#1- regrouper les fichier de meme type par dossier

# 2- deplacer chauqye type de fichier dans sous dossiers précis

from pathlib import Path

#on peut  creer les dossiers pour chaque type de dossier à trier

p = Path.home()
 
#a = p / "dossier_musique"

#a.mkdir(exist_ok=True)


#b = p / "dossier_video" 

#b.mkdir(exist_ok=True)


#c = p / "dossier_impages"
#c.mkdir(exist_ok=True)

#d = p / "autres"
#:d.mkdir(exist_ok=True)
# trier les fichier selon leurs extension

dirs = {
	".mp3": "dossier_musique",
	".wav":"dossier_musique",
	".flac" : "dossier_musique",
	".avi":"dossier_video",
	".mp4":"dossier_video",
	".gif" :"dossier_video",
	".bmp":"dossier_impages",
	".png":"dossier_impages",
	".jpg" : "dossier_impages",
	".txt": "Documents",
	".pptx":"Documents",
	".csv":"Documents",
	".xls":"Documents",
	".odp":"Documents",
	".pages": "Documents",
	}
donnees = p/"data"

files = [f for f in donnees.iterdir() if f.is_file()]
for f in files:
	output_dir = donnees/dirs.get(f.suffix,"autres")
	output_dir.mkdir(exist_ok=True)
	f.rename(output_dir / f.name)



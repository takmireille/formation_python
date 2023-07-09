import os
import subprocess
import csv

def create_directory_tree(root_dir, tree_structure):
    """
    Crée une arborescence de dossiers à partir d'une structure donnée.

    Arguments :
    root_dir -- le répertoire racine dans lequel créer l'arborescence
    tree_structure -- un dictionnaire représentant la structure de l'arborescence
    """
    try:
        for folder, subfolders in tree_structure.items():
            folder_path = os.path.join(root_dir, folder)
            os.makedirs(folder_path, exist_ok=True)

            if subfolders is not None:
                create_directory_tree(folder_path, subfolders)
        print("Arborescence de dossiers créée avec succès.")
    except Exception as e:
        print("Une erreur s'est produite :", str(e))

def create_groups(group_names):
    """
    Crée plusieurs groupes en utilisant la commande groupadd.
    Arguments :
    group_names -- une liste de noms de groupes à créer
    """
    try:
        for group_name in group_names:
            subprocess.run(["groupadd", group_name])
        print("Groupes créés avec succès.")
    except Exception as e:
        print("Une erreur s'est produite :", str(e))

def create_users_from_csv(csv_file, group_names):
    """
    Crée des utilisateurs à partir d'un fichier CSV et les associe aux groupes spécifiés.
    Arguments :
    csv_file -- le chemin vers le fichier CSV contenant les noms d'utilisateurs
    group_names -- une liste de noms de groupes auxquels les utilisateurs doivent être ajoutés
    """
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row

            for row in csv_reader:
                first_name = row[0].capitalize()
                last_name = row[1].lower()
                username = f"{first_name}.{last_name}"

                # Création de l'utilisateur
                subprocess.run(["useradd", "-m", "-s", "/bin/bash", username])

                # Ajout de l'utilisateur aux groupes existants
                for group_name in group_names:
                    subprocess.run(["usermod", "-aG", group_name, username])
        print("Utilisateurs créés avec succès et ajoutés aux groupes.")
    except Exception as e:
        print("Une erreur s'est produite :", str(e))

def extract_usernames_from_csv(input_file, output_file):
    """
    Extrait les noms d'utilisateur à partir d'un fichier CSV, les formate et les enregistre dans un fichier de sortie.
    Arguments :
    input_file -- le chemin vers le fichier CSV d'entrée
    output_file -- le nom du fichier de sortie (config.csv situé dans Systemes/Configuration/)
    """
    usernames = []

    with open(input_file, mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row:  # Vérifie si la ligne n'est pas vide
                name = row[0].strip()
                first_letter = name[0]
                username = first_letter.upper() + '.' + name.upper()
                usernames.append(username)

    output_dir = os.path.join("Systemes", "Configuration")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_file)

    with open(output_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Username'])  # Entête
        writer.writerows([[username] for username in usernames])
    print("Noms d'utilisateur extraits et enregistrés dans config.csv.")

# Structure d'arborescence
tree_structure = {
    'Documents': {
        'Compta': {
            'Factures': None,
            'Recus': None
        },
        'RH': {
            'Contrats': None,
            'CV': None
        },
        'Marketing': {
            'Campagne': None,
            'Images': None
        }
    },
    'Programmes': {
        'CodeSource': None,
        'Logiciels': {
            'Facturations': None,
            'GestionRH': None
        }
    },
    'Systemes': {
        'Backup': None,
        'Configuration': None
    }
}

root_dir = "./exo"
create_directory_tree(root_dir, tree_structure)

group_names = ["Compta", "Marketing", "RH", "Dev"]
create_groups(group_names)

csv_file = "./config.csv"
create_users_from_csv(csv_file, group_names)

input_file = "./config.csv"
output_file = "/home/tak/formation_python/python/projet_python1/projet1.csv/test/exo/Systemes/Configuration/config.csv"
extract_usernames_from_csv(input_file, output_file)
# des ameliorations restent encore à faire 
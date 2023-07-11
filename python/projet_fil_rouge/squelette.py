import csv
import os
import subprocess
# DEFINITION DES TACHES À FAIRE

def create_directory_tree(root_dir, tree_structure):
    """
    Déploie une arborescence de dossiers à partir d'une structure donnée.
    """
    try:
        for folder, subfolders in tree_structure.items():
            folder_path = os.path.join(root_dir, folder)
            os.makedirs(folder_path, exist_ok=True)

            if subfolders is not None:
                create_directory_tree(folder_path, subfolders)
        print("Arborescence de dossiers créée avec succès.")
    except PermissionError:
        print("Vous n'avez pas les permissions pour cette action.")
    except FileExistsError:
        print("Le dossier existe déjà.")
    except IOError:
        print("Une erreur s'est produite.")

########################################################################################################################################
def create_groups(group_names):
    """
    Crée plusieurs groupes en utilisant la commande groupadd.

    """
    try:
        for group_name in group_names:
            subprocess.run(["groupadd", group_name])
        print("Groupes créés avec succès.")
    except PermissionError:
        print("Vous n'avez pas les permissions pour cette action.")
    except IOError:
        print("Une erreur s'est produite lors de la création des groupes.")


###############################################################################################################################################
import csv
import subprocess
def create_users(fichier_csv):
    try:
        with open(fichier_csv, 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                nom = row['nom'].lower()
                prenom = row['prenom'].lower()
                groupe = row['groupe']
                username = prenom[0].lower() + nom
                password = "Toto"  # Mot de passe temporaire
                try:
                    subprocess.run(['useradd', '-m', '-p', password, '-G', groupe, username])
                    print(f"L'utilisateur '{username}' a été créé avec succès.")
                except :
                    print(f"Erreur lors de la création de l'utilisateur '{username}'.")
    
    except PermissionError:
        print("Vous n'avez pas les permissions nécessaires.")
    except FileNotFoundError:
        print(f"Le fichier '{fichier_csv}' n'a pas été trouvé.")
    

##################################################################################################################################################
def permission(fichier_csv):
    try:
        with open(fichier_csv, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                folder_path = row['folder_path']
                groupe_owner = row['groupe_owner']
                rights = row['rights']

                if folder_path and groupe_owner and rights:
                    os.chmod(folder_path, int(rights, 8))
                    print(f"Droits attribués au dossier '{folder_path}' : {rights}")
    
    except (PermissionError, FileNotFoundError) :
        print(f"Erreur lors de l'attribution des droits ")

###########################################################################################################################################
# EXECUTION
# Structure d'arborescence
tree_structure = {
    'Documents': {
        'Compta': {
            'Factures': None,
        },
        'Ressources_Humaines': {
            'Contrats': None,
        }
    }
}
root_dir = "./"
create_directory_tree(root_dir, tree_structure)
print (tree_structure)

group_names = ["Comptabilite", "Ressources_Humaines", "System"]
create_groups(group_names)

fichier_csv = './user.csv'
create_users(fichier_csv)

fichier_csv = './folder.csv'
permission(fichier_csv)

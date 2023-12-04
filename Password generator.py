import hashlib
import json

def modifier_le_mots_de_passe():
    try:
        with open("mots de passe.json", "r") as fichier:
            return json.load(fichier)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def enregistrer_le_mots_de_passe(mots_de_passe):
    with open("mots de passe.json", "w") as fichier:
        json.dump(mots_de_passe, fichier, indent=2)

def mots_de_passe_valide(motsdepasse):
    return all([
        len(motsdepasse) >= 8,
        any(char.isupper() for char in motsdepasse),
        any(char.islower() for char in motsdepasse),
        any(char.isdigit() for char in motsdepasse),
        any(char in "!@#$%^&*" for char in motsdepasse)
    ])

def ajout_mot_de_passe(nom_utilisateur, motsdepasse, mots_de_passe):
    if nom_utilisateur not in mots_de_passe:
        if mots_de_passe_valide(motsdepasse):
            mot_de_passe_crypte = hashlib.sha256(motsdepasse.encode()).hexdigest()
            mots_de_passe[nom_utilisateur] = mot_de_passe_crypte
            enregistrer_le_mots_de_passe(mots_de_passe)
            print(f"Mot de passe ajouté pour l'utilisateur {nom_utilisateur}.")
        else:
            print("Mot de passe invalide. Assurez-vous de respecter les exigences de sécurité.")
    else:
        print(f"Un mot de passe existe déjà pour l'utilisateur {nom_utilisateur}.")

def afficher_le_mots_de_passe(mots_de_passe):
    if not mots_de_passe:
        print("Aucun mot de passe enregistré.")
    else:
        print("Mots de passe enregistrés :")
        for nom_utilisateur, mot_de_passe_crypte in mots_de_passe.items():
            print(f"{nom_utilisateur}: {mot_de_passe_crypte}")

mots_de_passe = modifier_le_mots_de_passe()

while True:
    print("\nMenu :")
    print("1. Ajouter un nouveau mot de passe")
    print("2. Afficher les mots de passe")
    print("3. Quitter")
    
    choix = input("Choisissez une option (1/2/3) : ")

    if choix == "1":
        nom_utilisateur = input("Entrez le nom d'utilisateur : ")
        mot_de_passe = input("Entrez le mot de passe : ")
        ajout_mot_de_passe(nom_utilisateur, mot_de_passe, mots_de_passe)
    elif choix == "2":
        afficher_le_mots_de_passe(mots_de_passe)
    elif choix == "3":
        break
    else:
        print("Option invalide. Veuillez choisir 1, 2 ou 3.")
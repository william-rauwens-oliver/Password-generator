import hashlib
import json
import random

# Charger dans le fichier .json
def charger_mots_de_passe():
    try:
        with open("mots de passe.json", "r") as fichier:
            return json.load(fichier)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Enregistrer le MDP
def enregistrer_mots_de_passe(motsdepasse):
    with open("mots de passe.json", "w") as fichier:
        json.dump(mots_de_passe, fichier, indent=2)

# Valider le MDP
def valider_mot_de_passe(motsdepasse):
    return all([len(motsdepasse) >= 8, any(char.isupper() for char in motsdepasse),
                any(char.islower() for char in motsdepasse), any(char.isdigit() for char in motsdepasse),
                any(char in "!@#$%^&*" for char in motsdepasse)])

# Générer un MDP avec random
def generer_mot_de_passe():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(caracteres) for _ in range(12))

# Ajouter un MDP à l'utilisateur
def ajouter_mot_de_passe(nom, mot, mots):
    if nom not in mots:
        mot = generer_mot_de_passe() if mot.lower() == "random" else mot
        if not valider_mot_de_passe(mot):
            print("Mot de passe invalide. Assurez-vous de respecter les exigences de sécurité.")
            return
        mot_crypte = hashlib.sha256(mot.encode()).hexdigest()
        mots[nom] = mot_crypte
        enregistrer_mots_de_passe(mots)
        print(f"Mot de passe ajouté pour l'utilisateur {nom}.")
    else:
        print(f"Un mot de passe existe déjà pour l'utilisateur {nom}.")

# Afficher le MDP si on clique sur "2"
def afficher_mots_de_passe(mots):
    if not mots:
        print("Aucun mot de passe enregistré.")
    else:
        print("Mots de passe enregistrés :")
        for nom, mot_crypte in mots.items():
            print(f"{nom}: {mot_crypte}")
mots_de_passe = charger_mots_de_passe()

# Boucle principal + Menu
while True:
    print("\nMenu :")
    print("1. Ajouter un nouveau mot de passe")
    print("2. Afficher les mots de passe")
    print("3. Quitter")

    choix = input("Choisissez une option (1/2/3) : ")

    if choix == "1":
        nom_utilisateur = input("Nom d'utilisateur : ")
        mot_de_passe = input("Mot de passe ('random' pour générer aléatoirement) : ")
        ajouter_mot_de_passe(nom_utilisateur, mot_de_passe, mots_de_passe)
    elif choix == "2":
        afficher_mots_de_passe(mots_de_passe)
    elif choix == "3":
        break
    else:
        print("Option invalide. Veuillez choisir 1, 2 ou 3.")
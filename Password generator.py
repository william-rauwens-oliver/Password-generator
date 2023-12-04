import hashlib

def valide_mots_de_passe(mot_de_passe):
    return all([
        len(mot_de_passe) >= 8,
        any(char.isupper() for char in mot_de_passe),
        any(char.islower() for char in mot_de_passe),
        any(char.isdigit() for char in mot_de_passe),
        any(char in "!@#$%^&*" for char in mot_de_passe)
    ])

def Entrez_un_mots_de_passe():
    return input("Veuillez choisir un mot de passe : ")

def mots_de_passe_crypté(mot_de_passe):
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()

print("Le MDP doit contenir au moins huit caractères.")
print("Le MDP doit contenir au moins une lettre majuscule.")
print("Le MDP doit contenir au moins une lettre minuscule.")
print("Le MDP doit contenir au moins un chiffre.")
print("Le MDP doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")

while True:
    mot_de_passe = Entrez_un_mots_de_passe()
    if valide_mots_de_passe(mot_de_passe):
        mot_de_passe_crypte = mots_de_passe_crypté(mot_de_passe)
        print("Mot de passe valide. Mot de passe crypté avec SHA-256 :", mot_de_passe_crypte)
        break
    else:
        print("Mot de passe invalide. Assurez-vous de respecter les exigences de sécurité.")
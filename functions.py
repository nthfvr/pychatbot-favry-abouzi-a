import os
import math
def list_of_files(directory, extension):

    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)



# Fonction pour convertir le texte en minuscules
def minuscule():
    # on recupere les noms des fichier dans "speeches"
    files_names = list_of_files("speeches", "txt")

    # Parcours de chaque fichier
    for names in files_names:
        # Ouverture du fichier d'origine en mode lecture et du fichier résultant en mode écriture
        with open("speeches\\" + names, "r", encoding="utf-8") as fichier_president, open(
                "cleaned\\" + names + "cleaned.txt", "w", encoding="utf-8") as fichier_minuscule:
            # Lecture du contenu du fichier d'origine
            contenu = fichier_president.readlines()
            resultat = []

            # Parcours de chaque ligne dans le fichier d'origine
            for chaine in contenu:
                chaine_convertie = ""

                # Parcours de chaque caractère dans la ligne
                for caractere in chaine:
                    # Vérification si le caractère est une lettre majuscule
                    if 'A' <= caractere <= 'Z':
                        # Conversion en minuscule en ajustant le code ASCII
                        chaine_convertie += chr(ord(caractere) + (ord('a') - ord('A')))
                    else:
                        chaine_convertie += caractere

                # Ajout de la ligne convertie dans la liste des résultats
                resultat.append(chaine_convertie)

            # Écriture du contenu converti dans le fichier résultant
            for ligne in resultat:
                fichier_minuscule.write(ligne)


# Fonction pour supprimer la ponctuation
def ponctuation():
    texte_nettoye = ""
    list_ponctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                        '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    # Liste des noms de fichiers dans le répertoire "cleaned"
    files_names = list_of_files("cleaned", "txt")

    # Parcours de chaque fichier
    for names in files_names:
        # Ouverture du fichier à nettoyer en mode lecture
        with open("cleaned\\" + names, "r", encoding="utf-8") as fichier_cleaned:
            contenu = fichier_cleaned.readlines()

            # Parcours de chaque ligne dans le fichier à nettoyer
            for chaine in contenu:
                # Parcours de chaque caractère dans la ligne
                for caractere in chaine:
                    # Remplacement des tirets et apostrophes par des espaces
                    if caractere == '-' or caractere == "'":
                        texte_nettoye += " "
                    # Ajout du caractère dans le résultat s'il n'est pas dans la liste de ponctuation
                    elif caractere not in list_ponctuation:
                        texte_nettoye += caractere

            # Écriture du texte nettoyé dans le même fichier
            with open("cleaned\\" + names, "w", encoding="utf-8") as fichier_cleaned:
                fichier_cleaned.write(texte_nettoye)
                texte_nettoye = ""
minuscule()
ponctuation()
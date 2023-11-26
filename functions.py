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

def noms_presidents(noms_fichiers):
    # Renvoie une liste des noms des présidents à partir des noms des fichiers.

    liste_presidents = []

    # Supprime les prefixes "Nomination_" et suffixes ".txt"  des noms des fichiers.

    for i in range(len(noms_fichiers)):
        noms_fichiers[i] = noms_fichiers[i].strip("Nomination_")

        noms_fichiers[i] = noms_fichiers[i].strip(".txt")

        noms_fichiers[i] = noms_fichiers[i].strip("cleanedtxt")

    # Supprime tous les caractères qui ne font pas partie de l'alphabet dans les noms des présidents.

    for nom in noms_fichiers:

        nouveau_nom = ""

        for letter in nom:

            if letter.isalpha():
                nouveau_nom += letter

        liste_presidents.append(nouveau_nom)

    dictionnaire_presidents = dict.fromkeys(set(liste_presidents))

    return liste_presidents, dictionnaire_presidents
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


#4
def mot_max_occurrences(directory, extension,mot_recherche):
    # Liste des fichiers dans le répertoire avec l'extension spécifiée
    files_names = list_of_files(directory, extension)

    # Initialisation des variables pour le fichier avec le plus grand nombre d'occurrences
    fichier_max_occurrences = None
    max_occurrences = 0

    # Liste pour stocker les fichiers contenant le mot de recherche
    fichiers_avec_mot = []

    for filename in files_names:
        # Construit le chemin complet du fichier
        chemin_fichier = os.path.join(directory, filename)

        # Lis le contenu du fichier
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()

            # Utilise la fonction tf pour obtenir le nombre d'occurrences du mot de recherché
            occurrences_mot = tf(contenu).get(mot_recherche, 0)

            # Vérifie si le mot de recherche est présent dans le fichier
            if occurrences_mot > 0:
                fichiers_avec_mot.append(filename)

            # Met à jour le fichier avec le plus grand nombre d'occurrences si nécessaire
            if occurrences_mot > max_occurrences:
                max_occurrences = occurrences_mot
                fichier_max_occurrences = filename

    return  fichiers_avec_mot,fichier_max_occurrences

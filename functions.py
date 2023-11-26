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
    return liste_presidents,dictionnaire_presidents
  
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


def tf(chaine):
#Renvoie le nombre d'occurences de chaque mot dans un fichier

    dictionnaire_mot = {}
    liste_mots = chaine.split()
    liste_mots_sans_doublon = set(liste_mots)

    for word in liste_mots_sans_doublon:
        valeur = 0
        for mot_correspondant in liste_mots:
            if word == mot_correspondant:
                valeur += 1
        dictionnaire_mot[word] = valeur


    return dictionnaire_mot


import math


# Fonction qui calcule le score IDF pour chaque mot dans un répertoire de fichiers texte
def IDF(repertoire):
    # Récupération de la liste des noms de fichiers texte dans le répertoire
    files_names = list_of_files(repertoire, "txt")
    # Initialisation d'un ensemble pour stocker tous les mots uniques dans les documents
    set_mots = set([])
    # Initialisation du nombre total de documents
    nb_doc = 0
    # Boucle pour parcourir chaque fichier dans le répertoire
    for names in files_names:
        # Lecture du contenu du fichier
        with open(repertoire + names, "r", encoding="utf-8") as fichier_cleaned:
            contenu = fichier_cleaned.read()
            # Division du contenu en une liste de mots
            liste_de_mots = contenu.split()
            # Ajout de chaque mot à l'ensemble des mots uniques
            for mots in liste_de_mots:
                set_mots.add(mots)
            # Incrémentation du nombre de documents
            nb_doc += 1
    # Initialisation d'un dictionnaire pour stocker le nombre d'occurrences de chaque mot dans les documents
    dico_occurence_mot = {}
    # Boucle pour chaque mot unique dans l'ensemble de mots
    for mots in set_mots:
        # Initialisation du compteur d'occurrences pour le mot en cours
        cpt_occu_doc = 0
        # Boucle pour chaque fichier dans le répertoire
        for names in files_names:
            # Lecture du contenu du fichier
            with open(repertoire + names, "r", encoding="utf-8") as fichier_cleaned:
                contenu = fichier_cleaned.read()
                # Division du contenu en une liste de mots
                liste_de_mots = contenu.split()
                # Vérification de l'occurrence du mot dans le fichier
                if mots in liste_de_mots:
                    cpt_occu_doc += 1
        # Stockage du nombre d'occurrences du mot dans le dictionnaire
        dico_occurence_mot[mots] = cpt_occu_doc
    # Initialisation d'un dictionnaire pour stocker le score IDF de chaque mot
    score_idf = {}
    # Boucle pour chaque mot dans le dictionnaire d'occurrences
    for cle in dico_occurence_mot.keys():
        # Calcul du score IDF et stockage dans le dictionnaire
        score_idf[cle] = math.log10((nb_doc / (dico_occurence_mot[cle]+1)))
    # Retourne le dictionnaire final des scores IDF pour chaque mot
    return score_idf



def calculer_tfidf(repertoire):
    files_names = list_of_files(repertoire, "txt")
    set_mots = []
    for names in files_names:
        with open(repertoire + names, "r", encoding="utf-8") as fichier_cleaned:
            contenu = fichier_cleaned.read()
            liste_de_mots = contenu.split()
            for mots in liste_de_mots:
                set_mots.append(mots)
    set_mots=list(set(set_mots))


    idf=IDF("cleaned\\")

    matrice_tfidf = [[] for i in range(len(set_mots))]
    i=0
    for names in files_names:
        i=0
        mot_du_fichier = set([])
        with open("cleaned\\" + names, "r", encoding="utf-8") as fichier_cleaned:
            contenu = fichier_cleaned.read()
            tf_fichier = tf(contenu)
            liste_de_mots = contenu.split()
            for mots in liste_de_mots:
                mot_du_fichier.add(mots)
            for mot in set_mots:
                if mot in mot_du_fichier:
                    tf_mot=tf_fichier[mot]
                    idf_mot=idf[mot]
                    matrice_tfidf[i].append(tf_mot*idf_mot)
                else :
                    matrice_tfidf[i].append(0)
                i+=1
    #creation dictionaire pour associer le mot a ses scores tf-idf
    dico_matrice={}
    for i in range(len(set_mots)):
        dico_matrice[set_mots[i]]=matrice_tfidf[i]
    return [(matrice_tfidf), dico_matrice]



## Fonctionalité à developper
#1
tfidf=(calculer_tfidf("cleaned\\"))
def mot_non_important(repertoire):
    files_names=list_of_files(repertoire, "txt")
    list_mot_0 = [k for (k, val) in tfidf[1].items() if val==[0 for i in range(len(files_names))]]
    return (list_mot_0)

#2
def score_eleve(repertoire):
    files_names=list_of_files(repertoire, "txt")
    list_mot_0 = []
    dico_valeur_mot={}
    for (k, val) in tfidf[1].items():
        somme=0
        for valeur in val:
            somme+=valeur
        dico_valeur_mot[k]=somme/len(files_names)
    liste_valeur=list(dico_valeur_mot.values())
    maximum = liste_valeur[0]
    # Parcourir la liste pour trouver le maximum
    for element in liste_valeur:
        if element > maximum:
            maximum = element
    liste_mot_max=[]
    for keys in dico_valeur_mot.keys():
        if dico_valeur_mot[keys]==maximum:
            liste_mot_max.append(keys)
    return liste_mot_max

def rassemblement_discours():       #permet de rassembler les discours d'un meme president dans un meme fichier(pour fct3 et 6)
    nomspresident = noms_presidents(files_names)[0]
    index_element = nomspresident.index('GiscarddEstaing')
    nomspresident[index_element] = 'Giscard dEstaing'

    nomspresident = list(set(nomspresident))
    filesnames = list_of_files(("./cleaned"), "txt")

    for nom in nomspresident:
        for filename in filesnames:
            if nom in filename:
                with open("textes_president_en_un_meme_fichier\\" + nom + ".txt", "a", encoding="utf-8") as fichier1:
                    with open("cleaned\\" + filename, "r", encoding="utf-8") as fichier2:
                        contenu = fichier2.read()
                        fichier1.write(contenu)
rassemblement_discours()

#3
def mots_repete_chirac():
    occurrences = {}
    with open("textes_president_en_un_meme_fichier\\Chirac.txt", "r", encoding="utf-8") as fichier_cleaned:
        contenu = fichier_cleaned.read()
        liste_de_mots = contenu.split()
        for mot in liste_de_mots:
            if mot in occurrences:
                occurrences[mot] += 1
            else:
                occurrences[mot] = 1
    liste_valeur = list(occurrences.values())
    maximum = liste_valeur[0]
    # Parcourir la liste pour trouver le maximum
    for element in liste_valeur:
        if element > maximum:
            maximum = element
    liste_mot_max = []
    for keys in occurrences.keys():
        if occurrences[keys] == maximum:
            liste_mot_max.append(keys)
    return liste_mot_max

#4
def mot_max_occurrences(directory, extension, mot_recherche):
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
            occurrences_mot = tf(contenu).get(mot_recherche,0)

            # Vérifie si le mot de recherche est présent dans le fichier
            if occurrences_mot > 0:
                fichiers_avec_mot.append(filename)

            # Met à jour le fichier avec le plus grand nombre d'occurrences si nécessaire
            if occurrences_mot > max_occurrences:
                max_occurrences = occurrences_mot
                fichier_max_occurrences = filename

    return  fichiers_avec_mot,fichier_max_occurrences







#6
def mots_evoques():
    filesnames = list_of_files(("./cleaned"), "txt")
    set_mots = set([])
    for names in filesnames:
        with open("cleaned\\" + names, "r", encoding="utf-8") as fichier_cleaned:
            contenu = fichier_cleaned.read()
            # Division du contenu en une liste de mots
            liste_de_mots = contenu.split()
            # Ajout de chaque mot à l'ensemble des mots uniques
            for mots in liste_de_mots:
                set_mots.add(mots)
    # Initialisation d'un dictionnaire pour stocker le nombre d'occurrences de chaque mot dans les documents
    dico_occurence_mot = {}
    # Boucle pour chaque mot unique dans l'ensemble de mots

    filename = list_of_files("textes_president_en_un_meme_fichier\\", "txt")
    for mots in set_mots:
        # Initialisation du compteur d'occurrences pour le mot en cours
        cpt_occu_doc = 0
        # Boucle pour chaque fichier dans le répertoire
        for names in filename:
            # Lecture du contenu du fichier
            with open("textes_president_en_un_meme_fichier\\" + names, "r", encoding="utf-8") as fichier_cleaned:
                contenu = fichier_cleaned.read()
                # Division du contenu en une liste de mots
                liste_de_mots = contenu.split()
                # Vérification de l'occurrence du mot dans le fichier
                if mots in liste_de_mots:
                    cpt_occu_doc += 1
        # Stockage du nombre d'occurrences du mot dans le dictionnaire
        dico_occurence_mot[mots] = cpt_occu_doc
    liste = []
    mot_nonimportant = mot_non_important("cleaned\\")
    for mot, occu in dico_occurence_mot.items():
        if occu == len(filename) and mot not in mot_nonimportant:
            liste.append(mot)
    return liste
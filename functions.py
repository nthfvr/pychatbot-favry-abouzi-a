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


def tf(chaine):

    # Renvoie le nombre d'occurences de chaque mot dans un fichier

    # Cette fonction renvoie le nombre d'occurrences de chaque mot dans une chaîne de texte.


    # Initialisation d'un dictionnaire pour stocker le nombre d'occurrences de chaque mot
    dictionnaire_mot = {}

    # Séparation de la chaîne de texte en une liste de mots
    liste_mots = chaine.split()

    # Création d'une liste sans doublon pour obtenir tous les mots uniques dans la chaîne
    liste_mots_sans_doublon = set(liste_mots)

    # Parcours de la liste des mots uniques
    for word in liste_mots_sans_doublon:
        # Initialisation de la valeur du mot à 0
        valeur = 0

        # Parcours de la liste complète des mots pour compter les occurrences du mot actuel
        for mot_correspondant in liste_mots:
            # Si le mot actuel est égal au mot correspondant, incrémenter la valeur
            if word == mot_correspondant:
                valeur += 1


    return dictionnaire_mot


        # Stockage du nombre d'occurrences du mot dans le dictionnaire
        dictionnaire_mot[word] = valeur

    # Retour du dictionnaire contenant le nombre d'occurrences de chaque mot
    return dictionnaire_mot







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
        score_idf[cle] = math.log10((nb_doc / (dico_occurence_mot[cle] + 1)))
    # Retourne le dictionnaire final des scores IDF pour chaque mot
    return score_idf




# Fonction pour calculer la matrice TF-IDF
def calculer_tfidf(repertoire):
    # Obtention de la liste des noms de fichiers dans le répertoire donné avec l'extension "txt"
    files_names = list_of_files(repertoire, "txt")

    # Initialisation d'une liste pour stocker tous les mots uniques dans les fichiers
    set_mots = []

    # Parcours de chaque fichier dans le répertoire
    for names in files_names:
        # Lecture du fichier en cours
        with open(repertoire + names, "r", encoding="utf-8") as fichier_cleaned:
            contenu = fichier_cleaned.read()

            # Séparation du contenu du fichier en mots
            liste_de_mots = contenu.split()

            # Ajout de chaque mot à la liste des mots uniques
            for mots in liste_de_mots:
                set_mots.append(mots)

    set_mots = list(set(set_mots))



    # Élimination des doublons pour obtenir la liste finale de mots uniques
    set_mots = list(set(set_mots))

    # Initialisation de la variable IDF avec le répertoire cleaned

    idf = IDF("cleaned\\")

    # Initialisation d'une matrice vide pour stocker les scores TF-IDF de chaque mot pour chaque fichier
    matrice_tfidf = [[] for i in range(len(set_mots))]

    i = 0


    # Parcours de chaque fichier dans le répertoire pour calculer les scores TF-IDF

    for names in files_names:
        i = 0
        mot_du_fichier = set([])

        # Lecture du fichier en cours
        with open("cleaned\\" + names, "r", encoding="utf-8") as fichier_cleaned:
            contenu = fichier_cleaned.read()

            # Calcul du score TF pour chaque mot dans le fichier
            tf_fichier = tf(contenu)

            # Séparation du contenu du fichier en mots
            liste_de_mots = contenu.split()

            # Ajout de chaque mot du fichier à un ensemble
            for mots in liste_de_mots:
                mot_du_fichier.add(mots)

            # Calcul du score TF-IDF pour chaque mot unique par rapport à tous les mots uniques
            for mot in set_mots:
                if mot in mot_du_fichier:
                    tf_mot = tf_fichier[mot]
                    idf_mot = idf[mot]
                    matrice_tfidf[i].append(tf_mot * idf_mot)
                else:

                    matrice_tfidf[i].append(0)
                i += 1
    # creation dictionaire pour associer le mot a ses scores tf-idf
    dico_matrice = {}
    for i in range(len(set_mots)):
        dico_matrice[set_mots[i]] = matrice_tfidf[i]

                    # Si le mot n'est pas présent dans le fichier, le score TF-IDF est fixé à 0
                    matrice_tfidf[i].append(0)
                i += 1

    # Création d'un dictionnaire associant chaque mot à ses scores TF-IDF respectifs
    dico_matrice = {}
    for i in range(len(set_mots)):
        dico_matrice[set_mots[i]] = matrice_tfidf[i]

    # Retourne la matrice TF-IDF et le dictionnaire associatif

    return [(matrice_tfidf), dico_matrice]


## Fonctionalité à developper
tfidf = (calculer_tfidf("cleaned\\"))



# Fonction qui retourne une liste de mots non importants dans un répertoire donné
def mot_non_important(repertoire):
    # Récupère la liste des noms de fichiers ayant l'extension "txt" dans le répertoire spécifié
    files_names = list_of_files(repertoire, "txt")

    # Filtre les mots ayant une valeur TF-IDF égale à zéro pour tous les fichiers
    list_mot_0 = [mot for (mot, valeurs) in tfidf[1].items() if valeurs == [0 for i in range(len(files_names))]]

    # Retourne la liste des mots non importants
    return list_mot_0



# 2
def score_eleve(repertoire):
    # Obtient la liste des noms de fichiers dans le répertoire avec l'extension "txt"
    files_names = list_of_files(repertoire, "txt")

    # Initialise une liste vide pour stocker les mots clés
    list_mot_0 = []

    # Initialise un dictionnaire pour stocker la valeur TF-IDF moyenne de chaque mot clé
    dico_valeur_mot = {}

    # Calcule la valeur moyenne de TF-IDF pour chaque mot clé
    for (k, val) in tfidf[1].items():
        somme = 0

        # Calcule la somme des valeurs de TF-IDF pour chaque fichier
        for valeur in val:
            somme += valeur

        # Calcule la valeur moyenne et l'ajoute au dictionnaire
        dico_valeur_mot[k] = somme / len(files_names)

    # Convertit les valeurs du dictionnaire en une liste
    liste_valeur = list(dico_valeur_mot.values())

    # Initialise la valeur maximale avec la première valeur de la liste

    maximum = liste_valeur[0]

    # Parcourt la liste pour trouver la valeur maximale
    for element in liste_valeur:
        if element > maximum:
            maximum = element

    # Initialise une liste pour stocker les mots clés ayant la valeur maximale
    liste_mot_max = []

    # Parcourt le dictionnaire pour trouver les mots clés ayant la valeur maximale

    for keys in dico_valeur_mot.keys():
        if dico_valeur_mot[keys] == maximum:
            liste_mot_max.append(keys)

    # Retourne la liste des mots clés ayant la valeur TF-IDF maximale
    return liste_mot_max





def rassemblement_discours():   # permet de rassembler les discours d'un meme president dans un meme fichier(pour fct3 et 6)


    nomspresident = noms_presidents(files_names)[0]

    # Corrige une erreur de nom en remplaçant 'GiscarddEstaing' par 'Giscard dEstaing'
    index_element = nomspresident.index('GiscarddEstaing')
    nomspresident[index_element] = 'Giscard dEstaing'

    # Élimine les doublons dans la liste des noms de présidents
    nomspresident = list(set(nomspresident))

    # Obtient la liste des noms de fichiers dans le répertoire "./cleaned" avec l'extension ".txt"
    filesnames = list_of_files(("./cleaned"), "txt")

    # Parcourt chaque nom de président
    for nom in nomspresident:
        # Parcourt chaque nom de fichier dans le répertoire "./cleaned"
        for filename in filesnames:
            # Vérifie si le nom du président est présent dans le nom du fichier
            if nom in filename:
                # Ouvre le fichier de sortie en mode append
                with open("textes_president_en_un_meme_fichier\\" + nom + ".txt", "a",
                            encoding="utf-8") as fichier1:
                    # Ouvre le fichier source en mode lecture
                    with open("cleaned\\" + filename, "r", encoding="utf-8") as fichier2:
                        # Lit le contenu du fichier source
                        contenu = fichier2.read()
                        # Écrit le contenu dans le fichier de sortie
                        fichier1.write(contenu)


rassemblement_discours()


# 3
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


# 4
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
            occurrences_mot = tf(contenu).get(mot_recherche, 0)

            # Vérifie si le mot de recherche est présent dans le fichier
            if occurrences_mot > 0:
                fichiers_avec_mot.append(filename)

            # Met à jour le fichier avec le plus grand nombre d'occurrences si nécessaire
            if occurrences_mot > max_occurrences:
                max_occurrences = occurrences_mot
                fichier_max_occurrences = filename

    return fichiers_avec_mot, fichier_max_occurrences


# 5
def premier_president_ecologie_climat(directory, extension):
    # Liste des fichiers dans le répertoire avec l'extension spécifiée
    noms_fichier_local = list_of_files(directory, extension)

    # Initialiser le nom du premier président à parler d'écologie ou de climat
    premier_president_ecologie_climat = ""

    for filename in noms_fichier_local:
        liste_temp = []
        # Construire le chemin complet du fichier
        chemin_fichier = os.path.join(directory, filename)

        # Lire le contenu du fichier
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            contenu_president = fichier.read()
            # ajoute le nom du fichier à une liste pour pouvoir utiliser la fonction nom président dessus
            liste_temp.append(filename)
            # Vérifier si le fichier mentionne l'écologie ou le climat
            if 'écologie' in contenu_president or 'climat' in contenu_president:
                premier_president_ecologie_climat = noms_presidents(liste_temp)[0][0]
                break  # Sortir de la boucle dès qu'un président est trouvé

    return premier_president_ecologie_climat


# 6
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


def choixpartie1():


    print(
        "---------------------------------------------------------------------------------------------------------------------------")
    print("Sélectionner une option :")
    print("1 :Afficher la liste des mots les moins importants dans le corpus de documents")
    print("2 :Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé")
    print("3 :Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac")
    print(
        "4 :Indiquer le(s) fichiers(s) du(des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois")
    print("5 :Indiquer le premier président à parler du climat et/ou de l’écologie")
    print(
        "6 :Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués.")
<<<<<
    print("7 :Passer en mode chatbot")
    print(
        "---------------------------------------------------------------------------------------------------------------------------")
    liste_choix = [str(i) for i in range(1, 8)]
    #S'assure que le choix est valide
    choix = None
    while not choix in liste_choix:
        choix = input("Quel est votre choix: ")
    return choix



def token_quest(question):
    # Initialisation des variables
    question_str = ""
    chaine_convertie = ""

    # Liste des caractères de ponctuation à exclure

    list_ponctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                        '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    # Parcours de chaque caractère dans la question
    for caractere in question:
        # Vérification si le caractère est une lettre majuscule
        if 'A' <= caractere <= 'Z':
            # Conversion en minuscule en ajustant le code ASCII
            chaine_convertie += chr(ord(caractere) + (ord('a') - ord('A')))
        else:
            chaine_convertie += caractere

    # Parcours de chaque caractère converti
    for char in chaine_convertie:

        if char == "-" or char == "'":
            char = " "
        if char not in list_ponctuation:
            question_str += char
    liste_mot = question_str.split()
    return liste_mot,question_str

        # Remplacement des caractères spécifiques par des espaces
        if char == "-" or char == "'":
            char = " "
        # Exclusion des caractères de ponctuation
        if char not in list_ponctuation:
            question_str += char

    # Création d'une liste de mots en séparant la chaîne par les espaces
    liste_mot = question_str.split()

    # Retourne la liste de mots obtenue après le traitement
    return liste_mot, question_str 


def intersection(repertoire, question):
    # Liste des mots vides à exclure de l'analyse
    mots_vides = ['serait', 'tu', 'sera', 'aurons', 'eux', 'les', 'se', 'des', 'serons', 'mes',
                  'pourquoi', 'aurions', 'nos', 'auriez', 'qui', 'quand', 'quels', 'c', 'toi', 'auront', 'dans',
                  'suis', 's', 'auraient', "jusqu'à", 'tes', 'un', 'en', 'étant', 'vous', 'êtes', 'à', 'aux',
                  'il', 'si', 'pour', 'où', 'seraient', 'sa', 'été', 'au', 'vos', 'entre', 'elle', 'mais', 'seras',
                  'aurai', 'comment', 'votre', 'ses', 'es', 'serez', 'sur', 'quelles', 'lui', 'serions',
                  'aura', 'seront', 'j', 'et', 'quoi', 'le', 't', 'me', 'd', 'seriez', 'aurez', 'je', 'sont',
                  'quelle', 'ma', 'même', 'l', 'n', 'auras', 'notre', 'leur', 'y', 'par', 'avec', 'ton', 'te',
                  'sommes', 'une', 'nous', 'mon', 'de', 'serai', 'ta', 'on', 'ou', 'ces', 'son', 'ne', 'la',
                  'serais', 'm', 'a', 'sous', 'que', 'quel', 'aurais', 'aurait', 'moi', 'est', 'du',
                  'qu', 'ce']



    # Liste des noms de fichiers dans le répertoire avec l'extension "txt"

    files_names = list_of_files(repertoire, "txt")

    # Initialisation d'un ensemble pour stocker tous les mots uniques dans les documents
    set_mots = set([])

    # Boucle pour parcourir chaque fichier dans le répertoire

    liste_intersection = []
    liste_mot_question = token_quest(question)[0]


    for names in files_names:
        # Lecture du contenu du fichier
        with open(repertoire + names, "r", encoding="utf-8") as fichier_cleaned:
            contenu = fichier_cleaned.read()
            # Division du contenu en une liste de mots
            liste_de_mots = contenu.split()
            # Ajout de chaque mot à l'ensemble des mots uniques
            for mots in liste_de_mots:
                set_mots.add(mots)

    for mot_question in liste_mot_question:
        if mot_question in set_mots and mot_question not in mots_vides:
            liste_intersection.append(mot_question)
    return liste_intersection


def calculer_tfidf_question(question, ensemble_mots, idf_scores):
    # Calcul du score TF pour chaque mot dans la question
    tf_question = tf(token_quest(question)[1])

    # Initialisation du vecteur TF-IDF pour la question
    vecteur_tfidf_question = []

    # Calcul du score TF-IDF pour chaque mot dans l'ensemble de mots
    for mot in ensemble_mots:
        if mot in tf_question:
            tf_mot = tf_question[mot]
            idf_mot = idf_scores[mot]
            vecteur_tfidf_question.append(tf_mot * idf_mot)
        else:
            # Mettre un 0 pour les mots du corpus qui ne font pas partie de la question
            vecteur_tfidf_question.append(0)

    return vecteur_tfidf_question


def matricetransposee(dictionnaire):
    # Extraire la liste de mots et le nombre de documents
    mots = list(dictionnaire.keys())

    # Initialiser la matrice avec des listes vides
    matrice = [[] for i in range(8)]

    # Remplir la matrice avec les scores TF-IDF
    for mot in mots:
        for i in range(8):
            matrice[i].append(dictionnaire[mot][i])

    return matrice





def produitscalaire(vecteur1, vecteur2):
    # Calcule le produit scalaire de 2 vecteurs TF-IDF
    produitscalaire = 0
    for i in range(len(vecteur1)):
        produitscalaire += (vecteur1[i] * vecteur2[i])
    return produitscalaire


def norme(vecteur):

    # Retourne la norme d'un vecteur TF-IDF


    somme = 0
    for valeur in vecteur:
        somme += valeur ** 2
    norme = math.sqrt(somme)

    return norme


def similarite(vecteur1, vecteur2):

    # Calcule la similarité entre deux vecteurs TF-IDF

    similarite = (produitscalaire(vecteur1, vecteur2)) / (norme(vecteur1) * norme(vecteur2))

    return similarite


def document_pertinent(question):
    # Obtient la liste des noms de fichiers avec l'extension "txt" dans le répertoire "./speeches"
    files_names = list_of_files("./speeches", "txt")

   
    tfidf_corpus = tfidf[1]

  
    tfidf_question = calculer_tfidf_question(question, ensemble_mots, idf_scores_corpus)

    # Obtient l'intersection entre les mots de la question et les mots du répertoire "cleaned"
    inter = intersection("cleaned\\", token_quest(question)[1])

    # Initialisation des variables pour stocker la similarité maximale et le nom du document associé
    sim_max = [-1, files_names[0]]

    
    i = 0
    for names in files_names:
        # Initialisation d'une liste pour stocker les valeurs tf-idf pour les mots de l'intersection
        vecteur_inter = []
        for mot in inter:
            vecteur_inter.append(tfidf_corpus[mot][i])
        i += 1

        # Vérification pour éviter la division par zéro 
        if norme(vecteur_inter) != 0:
            
            sim = similarite(vecteur_inter, tfidf_question)

          
            if sim > (sim_max)[0]:
                sim_max[0] = sim
                sim_max[1] = names

    # Retourne le nom du document le plus pertinent
    doc = (sim_max)[1]
    return sim_max[1]

def trouvermot(question, ensemble_mots, idf_scores):
    vecteur_question = calculer_tfidf_question(question, ensemble_mots, idf_scores)
    max_element = vecteur_question[0]
    indice_max_element = 0

    for i in range(1, len(vecteur_question)):
        if vecteur_question[i] > max_element:
            max_element = vecteur_question[i]
            indice_max_element = i

    mot = ensemble_mots[indice_max_element]
    return mot


def trouver_phrase(mot, document):
    # Renvoie la première phrase où le mot apparaît
    with open(document, "r", encoding="utf-8") as f:
        contenu = f.read()

    phrases = contenu.split(".")

    for phrase in phrases:
        if mot in phrase:
            return phrase.strip() + "."
          
def mode_chatbot():
    running = True
    while running:

        print("---------------------------------------------------------------------------------------------------------------------------")
        question = input("Vous pouvez maintenant poser un question : ")
        if question == "QUIT":
            running = False
        question = token_quest(question)[1]
        mot = trouvermot(question,ensemble_mots,idf_scores_corpus)
        document = "speeches/Nomination_Chirac1.txt"
        print(trouver_phrase(mot,document))





def menu():
    running = True
    while running:
        print("Tapez'QUIT' pour retourner au menu")
        choix_utilisateur = choixpartie1()
        match choix_utilisateur:
            case "1":
                print("Liste des mots les moins importants: ")
                for value in mot_non_important("cleaned\\"):
                    print(value)

            case "2":
                print("liste des mots au score le plus élévé: ")
                for value in score_eleve("cleaned\\"):
                    print(value)

            case "3":
                print("liste des mots au score le plus élévé: ")
                for value in score_eleve("cleaned\\"):
                    print(value)

            case "4":
                resultat = mot_max_occurrences("cleaned", ".txt", "nation")
                print("Fichiers avec le mot 'nation' :", resultat[0])
                print("Fichier avec le plus grand nombre d'occurrences de 'nation' :", resultat[1])
            case "5":
                resultat = premier_president_ecologie_climat("cleaned", ".txt")
                if resultat:
                    print(f"Le premier président à parler d'écologie ou de climat est : {resultat}")
                else:
                    print("Aucun président ne mentionne l'écologie ou le climat.")
            case "6":
                print("Mots évoqués par tous les présidents")
                for value in mots_evoques():
                    print(value)
            case "7":
                mode_chatbot()
            case other:
                choix_utilisateur = choixpartie1()




#Assignation de variables
matricetransposee = matricetransposee(tfidf[1])
dictionnairetfidf = tfidf[1]
ensemble_mots = list(dictionnairetfidf.keys())
idf_scores_corpus = IDF("cleaned\\")










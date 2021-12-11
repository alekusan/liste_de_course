import json
import os
from os import listdir

choix_input = ["-Ajouter un produit",
"-Supprimer un produit",
"-Afficher votre liste",
"-Vider votre liste",
"-Enregistrer votre liste",
"-Quitter le programme\n"]

liste_course = []
choix_user = ""
produit = ""
quit = ""
js_file = ""
modify = False

CUR_DIR = os.path.dirname(__file__)      #---recherche du dossier parent
chemin_json = CUR_DIR                    #---assignation de la variable chemin_json avec le resultat de la const CUR_DIR
for i in listdir(chemin_json) :          #---si le fichier json existe, on charge les données
    if i == 'fichier.json' :
        js_file = "fichier.json"                                 #dans la liste_course sinon on entre dans le programme
        with open(i, "r") as f :
            liste_course = json.load(f)
    
while choix_user != "6" :
    produit = ""
    #Affichage des actions 
    for i,e in enumerate(choix_input):
        print(f"{int(i) + 1}{e}")
    choix_user = input("Veuillez choisir une action:")
    print("\n")
    #Si l'utilisateur tape "1", il ajoute son produit à la liste
    if choix_user == "1" :
        while produit == "" :
            produit = input("Veuillez entrer votre produit:")
            if produit != "" :
                liste_course.append(produit)
                print(f"le produit {produit} a été ajouté")
                modify = True
    #si l'utilisateur tape "2" il supprime un article, si l'article n'existe pas, l'utilisateur est renvoyé à l'affichage des actions
    elif choix_user == '2':
        produit = input("Veuillez entrer le produit à supprimer:")
        if produit in liste_course :
            liste_course.remove(produit)
            print(f"le produit {produit} a été supprimé de votre liste")
            modify = True
        else :
            print("il n'existe aucun produit de ce nom!")
    #si l'utilisateur tape "3", la liste de course s'affiche
    elif choix_user == "3" :
        if not liste_course :
            print("Il n'y a pas de produit dans la liste de course !\n")
        else :
            for i in liste_course :
                print(f"-{i}")
            print("\n")
    #si l'utilisateur tape 4, il vide la liste, si elle est deja vide, affiche un message
    elif choix_user == "4" :
        if not liste_course :
            print("Il n'y a pas de produit dans la liste de course !\n")
        else :
            liste_course.clear()
            print(" La liste a été vidé\n")
            modify = True
    #si l'utilisateur tape 5, il enregistre la liste, si la liste est vide, on revient au menu
    elif choix_user == "5" :
        if liste_course :
            with open(js_file, "w") as f :
                json.dump(liste_course, f, indent = 4)
            modify = False
        else : 
            print("Il n'y a rien à enregistrer, la liste est vide\n")
    # si l'utilisateur tape 6 et qu'il a modifié la liste sans enregistrer on lui demande, si il n'a rien modifié, rien ne se passe.
    elif choix_user == '6' :
        if modify == True :
            while quit != "1" and quit != "2":
                quit = input("Vous n'avez pas sauvegardé! voulez-vous le faire?\n-1 pour oui\n-2 pour non")
                print("\n")
                if quit == "1" :
                    if liste_course :
                        with open(js_file, "w") as f :
                            json.dump(liste_course, f, indent = 4)
                    else : 
                        print("Il n'y a rien à enregistrer, la liste est vide\nAu revoir !")
                if quit == "2" :
                    print("Au revoir !")
    else :
        print("Mauvaise saisie utilisateur")
choix_input = ["-Ajouter un produit",
"-Supprimer un produit",
"-Afficher votre liste",
"-Vider votre liste",
"-Enregistrer votre liste",
"-Quitter le programme\n"]

liste_course = ["pomme", "poire", "banane"]
choix_user = ""
produit = ""

while choix_user != "6" :
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
                print(liste_course[0])
    #si l'utilisateur tape "2" il supprime un article, si l'article n'existe pas, l'utilisateur est renvoyé à l'affichage des actions
    elif choix_user == '2':
        produit = input("Veuillez entrer le produit à supprimer:")
        if produit in liste_course :
            liste_course.remove(produit)
            print(f"le produit {produit} a été supprimé de votre liste")
        else :
            print("il n'existe aucun produit de ce nom!")
    #si l'utilisateur tape "3", la liste de course s'affiche
    elif choix_user == "3" :
        for i in liste_course :
            print(f"-{i}")
        print("\n")        

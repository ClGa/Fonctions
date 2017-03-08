def table(nb, max=10):
    """Fonction affichant la table de multiplication de nb de 0 à max
       Par défaut, max=10
       Si l'utilisateur rentre une valeur de max négative, la fonction prendra
       sa valeur absolue"""
    i=0
    max=abs(max)
    while i <= max:
        print(i, "*", nb, "=", i*nb)
        i+=1
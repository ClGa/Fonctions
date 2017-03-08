def puissance(a, n):
    """Fonction déterminant la n-eme puissance d'une valeur donnée par 
    l'utilisateur"""
    P=1
    for i in range(1, n+1):
        P*=a
        i+=1
    return P

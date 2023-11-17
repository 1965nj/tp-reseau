def trouver_chemins(graphe, depart, arrivee, chemin_actuel=[], chemins=[]):
    chemin_actuel.append(depart)

    if depart == arrivee:
        chemins.append(list(chemin_actuel))
    else:
        if depart not in graphe:
            return chemins

        voisins = graphe[depart]
        for voisin in voisins:
            if voisin not in chemin_actuel:
                trouver_chemins(graphe, voisin, arrivee, chemin_actuel, chemins)

    chemin_actuel.pop()

    return chemins

# Exemple d'utilisation
graphe = {
    'A': ['B', 'C'],
    'B': ['A','C', 'D'],
    'C': ['A','B','D','E'],
    'D': ['B','C','E','F'],
    'E': [ 'C','D','F'],
    'F': ['E','D']
}

depart = 'A'
arrivee = 'F'

tous_chemins = trouver_chemins(graphe, depart, arrivee)

print("Tous les chemins possibles de", depart, "à", arrivee, ":")
for chemin in tous_chemins:
    print(chemin)
from collections import deque

def trouver_chemins(graphe, depart, arrivee):
    queue = deque([(depart, [depart])])
    chemins = []

    while queue:
        nœud, chemin_actuel = queue.popleft()

        if nœud == arrivee:
            chemins.append(chemin_actuel)
        else:
            if nœud not in graphe:
                continue

            voisins = graphe[nœud]
            for voisin in voisins:
                if voisin not in chemin_actuel:
                    queue.append((voisin, chemin_actuel + [voisin]))

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
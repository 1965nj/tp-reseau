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
    'A': ['B', 'F'],
    'B': ['A','C', 'D','G'],
    'C': ['B','E'],
    'D': ['B','I'],
    'E': [ 'C','I'],
    'F': ['A','G','H'],
    'G': ['B','F','I'],
    'I': ['D','G','H','E'],
    'H': ['I','F']
}

depart = 'A'
arrivee = 'I'

tous_chemins = trouver_chemins(graphe, depart, arrivee)

print("Tous les chemins possibles de", depart, "à", arrivee, ":")
for chemin in tous_chemins:
    print(chemin)
class Graphe:
    def __init__(self):
        self.graph = {}

    # Méthode pour ajouter une arête au graphe
    def ajouter_arete(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    # Méthode récursive pour effectuer le parcours DFS
    def dfs(self, sommet, visite):
        # Marquer le sommet comme visité
        visite.add(sommet)
        print(sommet, end=' ')

        # Récursivement parcourir les sommets adjacents non visités
        if sommet in self.graph:
            for voisin in self.graph[sommet]:
                if voisin not in visite:
                    self.dfs(voisin, visite)

    # Méthode pour effectuer le parcours DFS à partir de chaque sommet non visité
    def parcours_dfs(self):
        visite = set()
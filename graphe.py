# Création d'un graphe
from parcours import Graphe;
g = Graphe()

# Ajout des arêtes
g.ajouter_arete('A', 'B')
g.ajouter_arete('A', 'C')
g.ajouter_arete('B', 'D')
g.ajouter_arete('B', 'E')
g.ajouter_arete('C', 'F')

# Parcours DFS du graphe
print("Parcours DFS du graphe :")
g.parcours_dfs()
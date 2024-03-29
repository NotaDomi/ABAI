# per modellare l'ambiente della mappa con le città
# potremmo usare una matrice con 0 e 1 per identificare
# la presenza o meno della connessione. Qui conviene usare il dizionario.
# A una chiave corrisponde una lista di città connesse.
import math

from src.GraphSearch import GraphSearch
from src.Problems import StreetProblem, StreetProblemInformed
from src.TreeSearch import TreeSearch
from src.strategies import Random, BreadthFirst, DepthLimited, DepthFirst, UniformCost, AStar, Greedy

environment = {
    'Andria': ['Corato', 'Trani'],
    'Corato': ['Ruvo', 'Trani', 'Andria', 'Altamura'],
    'Altamura': ['Corato', 'Ruvo', 'Modugno'],
    'Ruvo': ['Corato', 'Bisceglie', 'Terlizzi', 'Altamura'],
    'Terlizzi': ['Ruvo', 'Molfetta', 'Bitonto'],
    'Bisceglie': ['Trani', 'Ruvo', 'Molfetta'],
    'Trani': ['Andria', 'Corato', 'Bisceglie'],
    'Molfetta': ['Bisceglie', 'Giovinazzo', 'Terlizzi'],
    'Giovinazzo': ['Molfetta', 'Modugno', 'Bari', 'Bitonto'],
    'Bitonto': ['Modugno', 'Giovinazzo', 'Terlizzi'],
    'Bari': ['Giovinazzo', 'Modugno'],
    'Modugno': ['Bitonto', 'Giovinazzo', 'Altamura', 'Bari']
}

streets_coords = {
    'Andria': (41.2316, 16.2917),
    'Corato': (41.1465, 16.4147),
    'Altamura': (40.8302, 16.5545),
    'Ruvo': (41.1146, 16.4886),
    'Terlizzi': (41.1321, 16.5461),
    'Bisceglie': (41.243, 16.5052),
    'Trani': (41.2737, 16.4162),
    'Molfetta': (41.2012, 16.5983),
    'Giovinazzo': (41.1874, 16.6682),
    'Bitonto': (41.1118, 16.6902),
    'Modugno': (41.0984, 16.7788),
    'Bari': (41.1187, 16.852)
}


class Roads:
    def __init__(self, streets, coordinates):
        self.streets = streets
        self.coordinates = coordinates

    def distance(self, start, end):
        lat_a, long_a = self.coordinates[start]
        lat_b, long_b = self.coordinates[end]
        lat_diff = abs(lat_a - lat_b) * 111  # 111 per convertire da distanza in latitudine a distanza in km
        long_diff = abs(long_a - long_b) * 111  # 111 per convertire la distanza in longitudine in quella in km
        return math.sqrt((lat_diff ** 2) + (long_diff ** 2))


initial_state = 'Andria'
goal_state = 'Bari'
map = Roads(environment, streets_coords)
my_problem = StreetProblemInformed(initial_state=initial_state, goal_state=goal_state, environment=map)

strategies = [AStar(my_problem), Greedy(my_problem)]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    search = TreeSearch(problem=my_problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    try:
        print(node.path())
        print(node.cost)
        print("---------")
    except AttributeError:
        print("---------")
        pass

print("---------")

strategies = [AStar(my_problem), Greedy(my_problem)]

for strategy in strategies:
    search = GraphSearch(problem=my_problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    try:
        print(node.path())
        print(node.cost)
        print("---------")
    except AttributeError:
        print("---------")
        pass

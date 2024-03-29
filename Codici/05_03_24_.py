# per modellare l'ambiente della mappa con le città
# potremmo usare una matrice con 0 e 1 per identificare
# la presenza o meno della connessione. Qui conviene usare il dizionario.
# A una chiave corrisponde una lista di città connesse.
from src.GraphSearch import GraphSearch
from src.Problems import StreetProblem
from src.TreeSearch import TreeSearch
from src.strategies import Random, BreadthFirst, DepthLimited, DepthFirst, UniformCost

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

initial_state = 'Andria'
goal_state = 'Bari'
my_problem = StreetProblem(initial_state=initial_state, goal_state=goal_state, environment=environment)

strategies = [Random(), BreadthFirst(), DepthLimited(limit=3), UniformCost()]

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

strategies = [Random(), BreadthFirst(), DepthFirst(), DepthLimited(limit=7), UniformCost()]

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

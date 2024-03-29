from src.GraphSearch import GraphSearch
from src.Problems import EightPuzzle
from src.TreeSearch import TreeSearch
from src.strategies import DepthFirst, Random, BreadthFirst, DepthLimited, UniformCost, AStar

# Lo stato sarà la posizione del casella vuoto, le azioni rappresentano come si può "muovere" la casella vuota
# ['7', '2', '4', '5', '0', '6', '8', '3', '1']
# initial_state = ['7', '2', '4', '5', '0', '6', '8', '3', '1']
initial_state = [(2, 2), (0, 1), (2, 1), (1, 2), (0, 2), (1, 0), (1, 1), (0, 0), (2, 0)]
goal_state = [(2, 2), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]
# goal_state = ['1', '2', '3', '4', '5', '6', '7', '8', '0']
my_problem = EightPuzzle(initial_state, goal_state)

strategies = [AStar(my_problem), DepthLimited(limit=30)]

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

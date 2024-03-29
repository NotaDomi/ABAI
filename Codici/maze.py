from src.GraphSearch import GraphSearch
from src.Problems import Maze
from src.strategies import DepthFirst, BreadthFirst

environment = {
    '0,0': ['1,0'],
    '1,0': ['2,0', '0,0'],
    '2,0': ['2,1', '1,0'],
    '2,1': ['3,1', '2,2', '2,0'],
    '3,1': ['4,1', '2,1'],
    '4,1': ['4,0', '3,1'],
    '4,0': ['4,1'],
    '2,2': ['2,3', '2,1'],
    '2,3': ['1,3', '3,3'],
    '1,3': ['0,3', '2,3'],
    '0,3': ['0,2', '0,4', '1,3'],
    '0,2': ['0,3'],
    '0,4': ['0,3'],
    '3,3': ['3,4', '4,3', '2,3'],
    '3,4': ['3,3'],
    '4,3': ['3,3'],
}

initial_state = '0,0'
goal_state = '3,4'
my_problem = Maze(initial_state, goal_state, environment)

strategies = [DepthFirst(), BreadthFirst()]

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

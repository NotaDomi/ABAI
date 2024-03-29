from src.Problems import MazeProblem
from src.strategies import *
from src.TreeSearch import TreeSearch
from src.GraphSearch import GraphSearch
from src.Environments import Maze


def print_grid(height, width, p_walls, initial_state, goal_state, path):
    help_list = [initial_state]
    for el in path:
        if el == 'right':
            help_list.append((help_list[-1][0], help_list[-1][1] + 1))
        elif el == 'left':
            help_list.append((help_list[-1][0], help_list[-1][1] - 1))
        elif el == 'up':
            help_list.append((help_list[-1][0] - 1, help_list[-1][1]))
        elif el == 'down':
            help_list.append((help_list[-1][0] + 1, help_list[-1][1]))
    grid = ''
    for k in range(width):
        grid = grid + ' ---'
    grid = grid + '\n'
    for j in range(height):
        grid = grid + '|'
        for k in range(width):
            if (j, k) == initial_state:
                grid = grid + ' i |'
            elif (j, k) == goal_state:
                grid = grid + ' g |'
            elif (j, k) in p_walls:
                grid = grid + ' o |'
            elif (j, k) in help_list:
                grid = grid + ' * |'
            else:
                grid = grid + '   |'
        grid = grid + '\n'
    for k in range(width):
        grid = grid + ' ---'
    grid = grid + '\n'
    print(grid)


height = 5
width = 5
n_walls = 9
p_walls = [(0, 1), (1, 1), (1, 2), (3, 0), (3, 2), (4, 2), (1, 4), (2, 4), (4, 4)]

# model and load the environment

maze = Maze(height, width, n_walls, p_walls)
print(maze.create_environment())

initial_state = (0, 0)
goal_state = (3, 4)

maze_problem = MazeProblem(environment=maze,
                           initial_state=initial_state,
                           goal_state=goal_state)

strategies = [AStar(maze_problem), Greedy(maze_problem), Random(), BreadthFirst(), DepthLimited(limit=3), UniformCost()]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    search = TreeSearch(problem=maze_problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    try:
        print(node.path())
        print(node.cost)
        print_grid(height, width, p_walls, initial_state, goal_state, node.path())
    except AttributeError:
        pass

print("---------")

strategies = [AStar(maze_problem), Greedy(maze_problem), Random(), BreadthFirst(), DepthFirst(),
              DepthLimited(limit=6), UniformCost()]

for strategy in strategies:
    search = GraphSearch(problem=maze_problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    try:
        print(node.path())
        print(node.cost)
        print_grid(height, width, p_walls, initial_state, goal_state, node.path())
    except AttributeError:
        pass

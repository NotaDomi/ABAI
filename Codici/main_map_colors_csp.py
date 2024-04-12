from csp.problem import *
from csp.backtracking import *

problem = MapColors()
search = BackTracking(problem)

initial_state = {}
print(f'{search}')
print(search.run(initial_state))

problem = MapColors()
search = BackTracking(problem, var_criterion=minimum_remaining_values, value_criterion=least_constraining_value)

initial_state = {}
print(f'{search}')
print(search.run(initial_state))

problem = MapColors()
search = BackTracking(problem, var_criterion=degree_heuristic, value_criterion=least_constraining_value)

initial_state = {}
print(f'{search}')
print(search.run(initial_state))


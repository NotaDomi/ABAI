from src.Problems import EightQueensProblem
from src.local_search import *

problem = EightQueensProblem()
pool = list(i for i in range(0, 8))

searches = [HillClimbing(problem=problem), SimulatedAnnealing(problem=problem)]
for search in searches:
    # search = GeneticSearch(problem=problem, gene_pool=pool)

    result, state = search.run()

    print(result)
    print(problem.value(state))
    print(state)

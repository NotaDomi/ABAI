from src.Problems import EightQueensProblem
from src.local_search import *

problem = EightQueensProblem()
pool = list(i for i in range(0, 8))

searches = [HillClimbing(problem=problem), SimulatedAnnealing(problem=problem),
            GeneticSearch(problem=problem, p_mutation=0.1, population=100)]
for search in searches:
    # search = GeneticSearch(problem=problem, gene_pool=pool)

    result, state = search.run()

    print(result)
    print(problem.value(state))
    print(state)

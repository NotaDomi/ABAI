from src.Problems import EightQueensProblem
from src.local_search import *

problem = EightQueensProblem()
pool = list(i for i in range(0, 8))

search = HillClimbing(problem=problem)
for _ in range(1):
    # search = GeneticSearch(problem=problem, gene_pool=pool)

    result, state = search.run()

    print(result)
    print(problem.value(state))
    print(state)

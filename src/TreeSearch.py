from src.Node import Node


class TreeSearch:
    def __init__(self, problem, strategy=None):
        self.problem = problem
        self.strategy = strategy
        self.fringe = []

    def __repr__(self):
        return 'Tree search'

    def run(self):
        node = Node(state=self.problem.initial_state, parent=None, action=None, cost=0, depth=0)

        while True:
            if self.problem.goal_test(node.state):
                return 'Ok', node

            new_states = self.problem.successors(node.state)
            new_nodes = [node.expand(state=s, action=a, cost=self.problem.cost(node.state, a)) for s, a in new_states]

            self.fringe = self.fringe + new_nodes

            if len(self.fringe) != 0:
                self.fringe, node = self.strategy.select(self.fringe)
                if node is None:
                    return 'Fail', []
            else:
                return 'Fail', []


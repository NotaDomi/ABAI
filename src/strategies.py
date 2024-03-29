import random


class Random:  # Random strategy
    def __repr__(self):
        return 'Random strategy'

    @staticmethod
    def select(fringe):
        random.shuffle(fringe)
        node = fringe.pop(0)
        return fringe, node


class BreadthFirst:
    def __repr__(self):
        return 'Breadth first strategy'

    @staticmethod
    def select(fringe):
        node = fringe.pop(0)
        return fringe, node


class DepthFirst:
    def __repr__(self):
        return 'Depth first strategy'

    @staticmethod
    def select(fringe):
        node = fringe.pop()  # Se non specifico fa il pop dell'ultimo elemento
        return fringe, node


class DepthLimited:  # Dovrebbe andare bene, ma poi ricontrolla
    def __init__(self, limit):
        self.limit = limit

    def __repr__(self):
        return 'Depth limited strategy'

    def select(self, fringe):
        fringe = [n for n in fringe if n.depth <= self.limit]
        try:
            node = fringe.pop()  # Se non specifico fa il pop dell'ultimo elemento
        except IndexError:
            return [], None
        return fringe, node


class UniformCost:
    def __repr__(self):
        return 'Uniform cost strategy'

    @staticmethod
    def select(fringe):
        fringe = sorted(fringe, key=lambda x: x.cost)
        node = fringe.pop(0)
        return fringe, node


class Greedy:
    def __init__(self, problem):
        self.problem = problem

    def __repr__(self):
        return 'Greedy Search'

    def select(self, fringe):
        fringe = sorted(fringe, key=lambda x: self.problem.h(x.state))
        node = fringe.pop(0)
        return fringe, node


class AStar:
    def __init__(self, problem):
        self.problem = problem

    def __repr__(self):
        return 'AStar strategy'

    def select(self, fringe):
        fringe = sorted(fringe, key=lambda x: (self.problem.h(x.state) + x.cost))
        node = fringe.pop(0)
        return fringe, node

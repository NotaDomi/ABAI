class Node:
    def __init__(self, state, parent, action, depth, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost

    def __repr__(self):
        return f'({self.state})'

    def expand(self, state, action, cost=1):
        return Node(state=state,
                    parent=self,
                    action=action,
                    cost=self.cost + cost,
                    depth=self.depth + 1)

    def path(self):
        # return the path that we've followd till now
        path = []
        node = self
        while node.parent:
            path.append(node.action)
            node = node.parent
        path = list(reversed(path))
        return path

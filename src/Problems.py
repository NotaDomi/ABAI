# Formulazione del problema
import math
import random


class StreetProblem:
    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment

    def __repr__(self):
        return 'Street problem'

    def successors(self, state):  # return a couple state, action not a node
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        return self.environment[state]  # We return all the possible actions for a certain state in input

    def result(self, state=None, action=None):
        return action  # return the result performing an action(a state)

    def goal_test(self, state):
        return state == self.goal_state

    def cost(self, state, action):
        return 1  # In this case constant = 1


class StreetProblemInformed:
    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment

    def __repr__(self):
        return 'Informed street problem'

    def successors(self, state):  # return a couple state, action not a node
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        return self.environment.streets[state]  # We return all the possible actions for a certain state in input

    def result(self, state=None, action=None):
        return action  # return the result performing an action(a state)

    def goal_test(self, state):
        return state == self.goal_state

    def cost(self, state, action):
        reached_state = self.result(state, action)
        return self.environment.distance(state, reached_state)  # In this case constant = 1

    def h(self, state):
        lat_a, long_a = self.environment.coordinates[state]
        lat_b, long_b = self.environment.coordinates[self.goal_state]
        lat_diff = abs(lat_a - lat_b) * 111
        long_diff = abs(long_a - long_b) * 111
        return math.sqrt((lat_diff ** 2) + (long_diff ** 2))


class EightPuzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def __repr__(self):
        return 'Eight puzzle problem'

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        possible_actions = ['up', 'down', 'left', 'right']

        if state[0][0] == 0:
            possible_actions.remove("up")

        if state[0][0] == 2:
            possible_actions.remove("down")

        if state[0][1] == 0:
            possible_actions.remove("left")

        if state[0][1] == 2:
            possible_actions.remove("right")

        return possible_actions

    def result(self, state=None, action=None):
        result = state.copy()
        i = state[0]

        if action == 'up':
            tmp = i[0] - 1
            value = state.index((tmp, i[1]))
            result[value] = i
            result[0] = (tmp, i[1])

        if action == 'down':
            tmp = i[0] + 1
            value = state.index((tmp, i[1]))
            result[value] = i
            result[0] = (tmp, i[1])

        if action == 'left':
            tmp = i[1] - 1
            value = state.index((i[0], tmp))
            result[value] = i
            result[0] = (i[0], tmp)

        if action == 'right':
            tmp = i[1] + 1
            value = state.index((i[0], tmp))
            result[value] = i
            result[0] = (i[0], tmp)

        return result

    def goal_test(self, state):
        return state == self.goal_state

    def cost(self, state, action):
        return 1

    def h(self, state):
        newton = 0
        for i in range(0, 8):
            newton += abs(state[i][0] - self.goal_state[i][0]) + abs(state[i][1] - self.goal_state[i][1])
        return newton


class Maze:
    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment

    def __repr__(self):
        return 'Maze problem'

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        return self.environment[state]

    def result(self, state=None, action=None):
        return action

    def goal_test(self, state):
        return state == self.goal_state

    def cost(self, state, action):
        return 1


class MazeProblem:

    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment

    def successors(self, state):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        """
        Given a state returns the list of possible actions
        :param state: actual state
        :return: a list of actions
        """
        actionList = ['up', 'down', 'left', 'right']

        # managing maze borders
        if state[0] == 0:
            actionList.remove("up")

        if state[0] == self.environment.height - 1:
            actionList.remove("down")

        if state[1] == 0:
            actionList.remove("left")

        if state[1] == self.environment.width - 1:
            actionList.remove("right")

        for i in range(self.environment.n_walls):
            if (state[0] - 1, state[1]) == self.environment.p_walls[i]:
                actionList.remove("up")
            if (state[0] + 1, state[1]) == self.environment.p_walls[i]:
                actionList.remove("down")
            if (state[0], state[1] - 1) == self.environment.p_walls[i]:
                actionList.remove("left")
            if (state[0], state[1] + 1) == self.environment.p_walls[i]:
                actionList.remove("right")

        return actionList

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        if action == 'up':
            reached_state = (state[0] - 1, state[1])
        if action == 'down':
            reached_state = (state[0] + 1, state[1])
        if action == 'left':
            reached_state = (state[0], state[1] - 1)
        if action == 'right':
            reached_state = (state[0], state[1] + 1)
        return reached_state

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return state == self.goal_state

    def cost(self, state, action):
        """
        Given a state and an action returns the cost of the action
        :param state: a state
        :param action: an action
        :return: the cost of doing that action in that state
        """
        return 1

    def h(self, state):
        return abs(self.goal_state[0] - state[0]) + abs(self.goal_state[1] - state[1])


class EightQueensProblem:
    def __init__(self, initial_state=None):
        self.initial_state = initial_state
        if initial_state is None:
            self.initial_state = self.random()
        self.max_conflicts = sum([i for i in range(1, 8)])

    @staticmethod
    def random():
        chess = [random.randrange(0, 8) for _ in range(8)]
        return tuple(chess)

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        actions = []
        for col, row in enumerate(state):
            squares = list(range(0, 8))
            squares.remove(row)
            new_actions = list(zip([col] * len(squares), squares))
            actions.extend(new_actions)
        return actions

    def result(self, state=None, action=None):
        new_state = list(state)
        col, new_row = action
        new_state[col] = new_row
        return tuple(new_state)

    def cost(self, state, action):
        return 1

    def conflicts(self, state):
        conflicts = 0
        for col in range(8):
            queen = state[col]
            for col1 in range(col + 1, 8):
                queen1 = state[col1]
                if queen == queen1:
                    conflicts += 1
                if abs(queen - col) == abs(queen1 - col1) or queen + col == queen1 + col1:
                    conflicts += 1
        return conflicts

    def goal_test(self, state):
        return self.conflicts(state) == 0

    def value(self, state):
        return self.max_conflicts - self.conflicts(state)

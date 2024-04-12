from csp.constraints import *


class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def consistent(self, state):
        return all([c.check(state) for c in self.constraints])

    def complete(self, state):
        return len(state) == len(self.variables)

    def goal_test(self, state):
        return self.complete(state) and self.consistent(state)

    def assign(self, state, variable, value):
        if variable in self.variables and value in self.domains[variable]:
            new_state = dict(state)
            new_state[variable] = value
            return new_state
        raise ValueError

    def rollback(self, state, variable):
        if variable in self.variables:
            new_state = dict(state)
            del new_state[variable]
            return new_state
        raise ValueError

    def assignable_variables(self, state):
        return [variable for variable in self.variables if variable not in state]

    def legal_moves(self, state, variable):
        possible_values = self.domains[variable]
        return [value for value in possible_values if self.consistent(self.assign(state, variable, value))]

    def count_constraints(self, first_variable, second_variable):
        return sum([1 for c in self.constraints if first_variable in c.variables and second_variable in c.variables])

    def remaining_constraints(self, state, variable):
        remaining_variables = [var for var in self.variables if var not in state and var != variable]
        if remaining_variables:
            return sum([self.count_constraints(variable, rem_var) for rem_var in remaining_variables])
        else:
            return 0


class MapColors(CSP):
    def __init__(self):
        self.variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
        self.domains = {var: ['green', 'red', 'blue'] for var in self.variables}
        self.constraints = [
            DifferentValues(['WA', 'NT']),
            DifferentValues(['NT', 'WA']),
            DifferentValues(['WA', 'SA']),
            DifferentValues(['SA', 'WA']),
            DifferentValues(['SA', 'NT']),
            DifferentValues(['NT', 'SA']),
            DifferentValues(['SA', 'Q']),
            DifferentValues(['Q', 'SA']),
            DifferentValues(['SA', 'NSW']),
            DifferentValues(['NSW', 'SA']),
            DifferentValues(['SA', 'V']),
            DifferentValues(['V', 'SA']),
            DifferentValues(['Q', 'NT']),
            DifferentValues(['NT', 'Q']),
            DifferentValues(['NSW', 'Q']),
            DifferentValues(['Q', 'NSW']),
            DifferentValues(['V', 'NSW']),
            DifferentValues(['NSW', 'V'])
        ]

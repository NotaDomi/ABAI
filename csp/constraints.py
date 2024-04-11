class Constraint:
    def __init__(self, variables):
        self.variables = variables
        self.degree = len(variables)

    def check(self, state):
        True


class UnaryConstraint(Constraint):
    def __init__(self, variable):
        super(UnaryConstraint, self).__init__(variables=variable)
        self.variable = variable


class ValueConstraint(UnaryConstraint):
    def __init__(self, variable, accepted_values):
        super(ValueConstraint, self).__init__(variable=variable)
        self.accepted_values = accepted_values

    def check(self, state):
        if self.variable in state:
            return state[self.variable] in self.accepted_values
        return True


class DifferentValues(Constraint):
    def check(self, state):
        values = [state[var] for var in self.variables if var in state]
        return len(values) == len(set(values))

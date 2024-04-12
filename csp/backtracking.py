import random


def random_variable(problem, state):
    assignable_vars = problem.assignable_variables(state)
    if assignable_vars:
        random.shuffle(assignable_vars)
        return assignable_vars.pop()
    return None


def minimum_remaining_values(problem, state):
    return min(problem.assignable_variables(state), key=lambda v: len(problem.legal_moves(state, v)))


def degree_heuristic(problem, state):
    return max(problem.assignable_variables(state), key=lambda v: problem.remaining_constraints(state, v))


def random_assignment(problem, state, variable):
    possible_values = problem.domains[variable]
    random.shuffle(possible_values)
    return possible_values


def least_constraining_value(problem, state, variable):
    assignable_values = problem.domains[variable]
    return sorted(assignable_values,
                  key=lambda v: -sum([len(problem.legal_moves(problem.assign(state, variable, v), var))
                                      for var in problem.assignable_variables(problem.assign(state, variable, v))]))


class BackTracking:
    def __init__(self, problem, var_criterion=None, value_criterion=None):
        self.problem = problem
        if var_criterion is None:
            var_criterion = random_variable
        self.var_criterion = var_criterion
        if value_criterion is None:
            value_criterion = random_assignment
        self.value_criterion = value_criterion

    def __repr__(self):
        return 'Backtracking'

    def run(self, state):
        if self.problem.goal_test(state):
            return state

        variable = self.var_criterion(self.problem, state)
        if variable is None:
            return False

        values = self.value_criterion(self.problem, state, variable)
        for value in values:
            new_state = self.problem.assign(state, variable, value)
            if self.problem.consistent(new_state):
                state = dict(new_state)
                result = self.run(dict(state))

                if result:
                    return result
                else:
                    state = self.problem.rollback(state, variable)
        return False

    def forward_checking(self, state, domains):
        new_domains = dict(domains)
        for var in self.problem.variables:
            new_domains[var] = self.problem.legal_moves(state, var)
        return new_domains

    def run_with_forward_checking(self, state, domains):
        # check if the state is the goal state
        if self.problem.goal_test(state):
            return state

        # check for domain failure with forward checking
        if [] in domains.values():
            return False

        # choose the next variable to be assigned
        variable = self.var_criterion(self.problem, state)
        if variable is None:
            return False

        # order the values with a desired order
        values = self.value_criterion(self.problem, state, variable)

        # for all the values
        for value in values:

            # assign the value and reach a new state
            new_state = self.problem.assign(state=state,
                                            variable=variable,
                                            value=value)

            if self.problem.consistent(new_state):
                state = dict(new_state)

                # apply forward checking
                new_domains = self.forward_checking(state, domains)
                del(new_domains[variable])   # we delete the entry of the dictionary having the variable to which a value has been already assigned as key

                # run the search on the new state
                result = self.run_with_forward_checking(dict(state), new_domains)

                # if succeeds return the solution
                if result:
                    return result
                else:
                    # if the result is a failure cancel the assignment
                    state = self.problem.rollback(state, variable)

        # if there is no possible value a failure
        return False



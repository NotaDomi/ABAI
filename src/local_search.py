import math
import random
from src.Node import Node


class HillClimbing:
    def __init__(self, problem):
        self.problem = problem

    def run(self):
        node = Node(state=self.problem.initial_state, parent=None, action=None, cost=0, depth=0)

        while True:
            new_states = self.problem.successors(node.state)

            best_neighbor, best_action = max(new_states, key=lambda x: self.problem.value(x[0]))

            if self.problem.value(node.state) >= self.problem.value(best_neighbor):
                return 'Ok', node.state

            node = node.expand(state=best_neighbor, action=best_action, cost=1)


class SimulatedAnnealing:

    def __init__(self, problem, lam=0.001, min_temp=0):
        self.problem = problem
        self.lam = lam
        self.min_temp = min_temp

    def exponential_schedule(self, temp, time):
        return temp * math.exp(-self.lam * time)

    def run(self, initial_temp=100):
        time = 0
        temp = initial_temp
        node = Node(state=self.problem.initial_state, parent=None, action=None, cost=0, depth=0)

        while temp > self.min_temp:
            new_states = self.problem.successors(node.state)  # finding the nighbour

            selected_neighbor, selected_action = random.choice(new_states)

            score_diff = self.problem.value(selected_neighbor) - self.problem.value(
                node.state)  # delta_E of the formula

            if score_diff > 0 or random.uniform(0, 1) < math.exp(score_diff / temp):
                node = node.expand(state=selected_neighbor, action=selected_action, cost=1)

            temp = self.exponential_schedule(temp, time)

            time += 1

        return 'Ok', node.state


class GeneticSearch:  # with sequence of numbers/characters
    def __init__(self, problem, population=1000, generations=100, p_mutation=0.1, gene_pool=None):
        self.problem = problem
        self.population = population
        self.generations = generations
        self.couples = int(self.population / 2)
        self.p_mutations = p_mutation
        self.gene_pool = gene_pool

    def select(self, population):
        fitnesses = list(map(self.problem.value, population))
        return random.choices(population=population, weights=fitnesses, k=2)

    def crossover(self, couple):
        parent_a, parent_b = couple
        split = random.randint(0, len(parent_a))
        return tuple(list(parent_a[:split]) + list(parent_b[split:]))

    def mutation(self, state):
        if random.uniform(0, 1) > self.p_mutations and self.gene_pool:
            return state
        new_state = list(state)
        new_state[random.randint(0, len(state) - 1)] = random.choice(self.gene_pool)
        return tuple(new_state)

    def run(self):
        population = [self.problem.random() for _ in range(self.population)]

        for e in range(self.generations):
            new_generation = [
                self.mutation(
                    self.crossover(
                        self.select(population)
                    )
                )
                for _ in range(self.population)]

            population = new_generation
        return 'Ok', max(population, key=lambda x: self.problem.value(x))

import math
import random
from solver.doubleminimumspanningtree import DoubleMinimumSpanningTree
from solver.basesolver import BaseSolver


class AntColonySystem(BaseSolver):

    def __init__(self):
        super().__init__()
        self.ALPHA = 1.0
        self.BETA = 5.0
        self.RHO_G = 0.9
        self.DETERMINISTIC_PROBABILTITY = 0.7
        self.Q = 1.0
        self.ANT_NUMBER = 50
        self.MAX_ITER = 30
        self.initial_pheromone = 0.1

    def solve(self, city_list):
        start = self.start_time()
        self.initial_pheromone = 1 / (len(city_list) * DoubleMinimumSpanningTree().solve(city_list)[1])
        ground = Ground(city_list, self.create_rout_cost_matrix(city_list), self.init_pheromone_matrix(len(city_list)))
        ants = self.create_ants(ground)
        best_ant = self.run(ground, ants)
        cost = self.cost_evaluate(best_ant.route, city_list)
        end = self.end_time(start)
        return (best_ant.route, cost, end)

    def create_ants(self, ground):
        ants = []
        for _ in range(self.ANT_NUMBER):
            ant = Ant(ground, random.randrange(len(ground.city_list)), self.ALPHA, self.BETA, self.initial_pheromone, self.DETERMINISTIC_PROBABILTITY)
            ants.append(ant)
        return ants

    def run(self, ground, ants):
        best_ant = None
        min_cost = self.max_cost
        for _ in range(self.MAX_ITER):
            for ant in ants:
                ant.run()
                if ant.tour_cost < min_cost:
                    best_ant = ant
                    min_cost = ant.tour_cost
            self.update_pheromone(ground, best_ant)
        return best_ant

    def update_pheromone(self, ground, best_ant):
        for i in range(len(ground.city_list)):
            for j in range(i, len(ground.city_list)):
                if i != j:
                    pheromone = ground.city_pheromone_matrix[i][j] * self.RHO_G
                    ground.city_pheromone_matrix[i][j] = pheromone
                    ground.city_pheromone_matrix[j][i] = pheromone
        for i in range(1, len(best_ant.route)):
            source_city = best_ant.route[i]
            destination_city = best_ant.route[i - 1]
            delta = 1 / best_ant.tour_cost
            ground.city_pheromone_matrix[source_city][destination_city] += delta
            ground.city_pheromone_matrix[destination_city][source_city] += delta

    def create_rout_cost_matrix(self, city_list):
        city_number = len(city_list)
        route_cost_matrix = [[0 for _ in range(city_number)] for _ in range(city_number)]
        for src_city_coordinate in range(city_number):
            for dist_city_coodinate in range(city_number):
                route_cost_matrix[src_city_coordinate][dist_city_coodinate] = self.disc(city_list[src_city_coordinate], \
                                                                                        city_list[dist_city_coodinate])
        return route_cost_matrix

    def init_pheromone_matrix(self, city_number):
        return [[self.initial_pheromone for _ in range(city_number)] for _ in range(city_number)]

class Ground(object):
    def __init__(self, city_list, city_cost_matrix, city_pheromone_matrix):
        super().__init__()
        self.city_list = [i for i in range(len(city_list))]
        self.city_cost_matrix = city_cost_matrix
        self.city_pheromone_matrix = city_pheromone_matrix

class Ant(object):
    def __init__(self, ground, initial_city, alpha, beta, initial_pheromone, deterministic_probability):
        super().__init__()
        self.RHO_L = 0.9
        self.base_t = initial_pheromone
        self.ground = ground
        self.initial_city = initial_city
        self.alpha = alpha
        self.beta = beta
        self.deterministic_probability = deterministic_probability
        self.next_city = -1
        self.current_city = initial_city
        self.tour_cost = 0.0
        self.route = []

    def setup_run(self):
        self.next_city = -1
        self.current_city = self.initial_city
        self.tour_cost = 0.0
        self.route = []

    def run(self):
        self.setup_run()
        unreached_city_list = [i for i in self.ground.city_list]
        unreached_city_list.remove(self.initial_city)
        while len(unreached_city_list) > 0:
            self.next_city = self.select_next_city(unreached_city_list)
            self.route.append(self.current_city)
            self.tour_cost += self.ground.city_cost_matrix[self.current_city][self.next_city]
            self.current_city = self.next_city
            unreached_city_list.remove(self.current_city)
        self.tour_cost += self.ground.city_cost_matrix[self.current_city][self.initial_city]
        self.route.extend([self.current_city, self.initial_city])
        return self.route

    def select_next_city(self, unreached_city_list):
        rand = random.random()
        next_city = 0
        costs = []
        for city in unreached_city_list:
            costs.append(self.get_tract_value(self.current_city, city))
        cdf = self.create_cdf(costs)
        if rand <= self.deterministic_probability:
            costs_with_index = [(index, cost) for (index, cost) in enumerate(costs)]
            next_city = list(reversed(sorted(costs_with_index, key=lambda x:x[1])))[0][0]
        else:
            rand = random.random()
            while cdf[next_city] < rand:
                next_city += 1
        self.update_pheromone(next_city)
        return unreached_city_list[next_city]

    def update_pheromone(self, next_city):
        pheromone = self.ground.city_pheromone_matrix[self.current_city][next_city] * self.RHO_L + \
                    self.base_t * (1 - self.RHO_L)
        self.ground.city_pheromone_matrix[self.current_city][next_city] = pheromone
        self.ground.city_pheromone_matrix[next_city][self.current_city] = pheromone

    def get_tract_value(self, source_city, destination_city):
        pheromone = self.ground.city_pheromone_matrix[source_city][destination_city]
        cost = self.ground.city_cost_matrix[source_city][destination_city]
        return math.pow(pheromone, self.alpha) * math.pow(1.0/cost, self.beta)

    def create_cdf(self, costs):
        total = sum(costs)
        cdf = []
        probability = 0.0
        for cost in costs:
            probability += cost
            cdf.append(probability/total)
        return cdf
import math
import random
from solver.basesolver import BaseSolver


class AntSystem(BaseSolver):

    def __init__(self):
        super().__init__()
        self.ALPHA = 1.0
        self.BETA = 5.0
        self.RHO = 0.8
        self.INITIAL_PHEROMONE = 0.1
        self.Q = 1.0
        self.ANT_NUMBER = 20
        self.MAX_ITER = 30

    def solve(self, city_list):
        start = self.start_time()
        ground = Ground(city_list, self.create_rout_cost_matrix(city_list), self.init_pheromone_matrix(len(city_list)))
        self.ANT_NUMBER = len(city_list)
        ants = self.create_ants(ground)
        best_ant = self.run(ground, ants)
        cost = self.cost_evaluate(best_ant.route, city_list)
        end = self.end_time(start)
        return (best_ant.route, cost, end)

    def create_ants(self, ground):
        ants = []
        for _ in range(self.ANT_NUMBER):
            ant = Ant(ground, random.randrange(len(ground.city_list)), self.ALPHA, self.BETA)
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
            self.update_pheromone(ground, ants)
        return best_ant

    def update_pheromone(self, ground, ants):
        for i in range(len(ground.city_list)):
            for j in range(i, len(ground.city_list)):
                if i != j:
                    pheromone = ground.city_pheromone_matrix[i][j] * self.RHO
                    ground.city_pheromone_matrix[i][j] = pheromone
                    ground.city_pheromone_matrix[j][i] = pheromone
        for ant in ants:
            for i in range(1, len(ant.route)):
                source_city = ant.route[i]
                destination_city = ant.route[i - 1]
                delta = self.Q / ant.tour_cost
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
        return [[self.INITIAL_PHEROMONE for _ in range(city_number)] for _ in range(city_number)]

class Ground(object):
    def __init__(self, city_list, city_cost_matrix, city_pheromone_matrix):
        super().__init__()
        self.city_list = [i for i in range(len(city_list))]
        self.city_cost_matrix = city_cost_matrix
        self.city_pheromone_matrix = city_pheromone_matrix

class Ant(object):
    def __init__(self, ground, initial_city, alpha, beta):
        super().__init__()
        self.ground = ground
        self.initial_city = initial_city
        self.alpha = alpha
        self.beta = beta
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
        costs = []
        for city in unreached_city_list:
            costs.append(self.get_tract_value(self.current_city, city))
        cdf = self.create_cdf(costs)
        rand = random.random()
        index = 0
        while cdf[index] < rand:
            index += 1
        return unreached_city_list[index]

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
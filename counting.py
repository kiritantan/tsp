from basesolver import BaseSolver
import itertools


class Counting(BaseSolver):
    def __init__(self):
        self.city_number_permutation = []
        super().__init__()

    def solve(self, city_list, isVisualized=False):
        self.calc_permutation(len(city_list))
        super().create_matrix(city_list)
        for elem in self.city_number_permutation:
            cost = self.cost_evaluate(elem)
            if self.max_cost > cost:
                print("{0} -> {1}".format(self.max_cost, cost))
                self.max_cost = cost
                self.circuit = elem
        return self.circuit

    def cost_evaluate(self, city_number_list):
        sum = 0
        sum_of_city = len(city_number_list) - 1
        for index in range(0,sum_of_city):
            sum += self.city_cost_matrix[city_number_list[index]][city_number_list[(index+1)]]
        return sum

    def calc_permutation(self, number_of_city=1):
        self.city_number_permutation = []
        city_number_list = [x for x in range(0, number_of_city)][1:]
        city_number_permutation = list(map(list, itertools.permutations(city_number_list)))
        for elem in city_number_permutation:
            elem.insert(0, 0)
            elem.append(0)
        self.city_number_permutation = city_number_permutation
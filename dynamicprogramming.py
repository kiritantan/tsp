from basesolver import BaseSolver
import sys

class DynamicProgramming(BaseSolver):
    def __init__(self):
        self.city_set_matrix = []
        self.SMAX = 0
        self.city_number = 0
        super().__init__()

    def solve(self, city_list):
        self.city_number = len(city_list)
        self.SMAX = 1 << self.city_number
        self.city_set_matrix = [[sys.maxsize for _ in range(self.SMAX)] for _ in range(self.city_number)]

        for i in range(self.city_number):
            self.city_set_matrix[i][0] = 0

        for i in range(self.city_number-1):
            self.city_set_matrix[i][1 << i] = super().disc(city_list[i], city_list[self.city_number-1])

        for s in range(1, self.SMAX):
            for i in range(self.city_number):
                if not ((1 << i) & s): continue
                for j in range(self.city_number):
                    if ((1 << j) & s): continue
                    tmp = self.city_set_matrix[i][s] + super().disc(city_list[i], city_list[j])
                    if tmp < self.city_set_matrix[j][s | (1 << j)]:
                        self.city_set_matrix[j][s | (1 << j)] = tmp

        return ((self.city_set_matrix[self.city_number - 1][self.SMAX - 1]), )

#    def get_route(self, city_cost_matrix, city_number, start):
#        route = [start + 1]
#        v = 1 << start
#        p = start

#        while len(route) < city_number:
#            (_, q) = city_cost_matrix[v][p]
#            route.append(q+1)
#            v |= (1 << a)
#            p = q

#        route.append(start+1)
#        return route


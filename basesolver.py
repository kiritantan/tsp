from math import sqrt
import sys


class BaseSolver(object):

    def __init__(self):
        self.city_cost_matrix = []
        self.max_cost = sys.maxsize
        self.circuit = []

    def solve(self, city_list):
        raise Exception("plese set solve algorithm")

    #O(n^2)
    def create_matrix(self, city_list):
        self.city_cost_matrix = []
        for i in range(0, len(city_list)):
            dist_list = []
            for j in range(0, len(city_list)):
                dist_list.append(self.disc(city_list[i],city_list[j]))
            self.city_cost_matrix.append(dist_list)

    #O(1)
    def disc(self, city1, city2):
        dx = city1[0]-city2[0]
        dy = city1[1]-city2[1]
        return int(sqrt(dx**2+dy**2)+0.5)



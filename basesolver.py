from math import sqrt
import sys


class BaseSolver(object):

    def __init__(self):
        self.city_cost_matrix = []
        self.max_cost = sys.maxsize
        self.circuit = []

    def solve(self, city_list):
        raise Exception("plese set solve algorithm")

    #O(1)
    def disc(self, city1: object, city2: object) -> object:
        dx = city1[0]-city2[0]
        dy = city1[1]-city2[1]
        return int(sqrt(dx**2+dy**2)+0.5)

    def sort_circuit(self, circuit):
        index = circuit.index(0)
        return circuit[index:] + circuit[:index]

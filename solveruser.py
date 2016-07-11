import matplotlib.pyplot as plt

from solver.annealing import Annealing
from solver.basesolver import BaseSolver
from solver.counting import Counting
from solver.doubleminimumspanningtree import DoubleMinimumSpanningTree
from solver.dynamicprogramming import DynamicProgramming
from solver.hillclimbing import HillClimbing
from solver.antsystem import AntSystem
from solver.antcolonysystem import AntColonySystem
from solver.fireflysystem import FireFlySystem
from solver.nearestinsertion import NearestInsertion
from solver.farthestinsertion import FarthestInsertion
from solvername import SolverName


class SolverUser():
    def __init__(self, solver=SolverName.BaseSolver):
        if solver.name == "Counting":
            self.solver = Counting()
        elif solver.name == "DynamicProgramming":
            self.solver = DynamicProgramming()
        elif solver.name == "Annealing":
            self.solver = Annealing()
        elif solver.name == "DoubleMinimumSpanningTree":
            self.solver = DoubleMinimumSpanningTree()
        elif solver.name == "HillClimbing":
            self.solver = HillClimbing()
        elif solver.name == "AntSystem":
            self.solver = AntSystem()
        elif solver.name == "AntColonySystem":
            self.solver = AntColonySystem()
        elif solver.name == "FireFlySystem":
            self.solver = FireFlySystem()
        elif solver.name == "NearestInsertion":
            self.solver = NearestInsertion()
        elif solver.name == "FarthestInsertion":
            self.solver = FarthestInsertion()
        else:
            self.solver = BaseSolver()

    # 問題を解き、結果を最短系で都市をつなげたグラフで表示する
    def solve_with_graph(self, city_list):
        circuit = self.__solve(city_list)[0]
        graph_dot_x = []
        graph_dot_y = []
        for vertex in circuit:
            graph_dot_x.append(city_list[vertex][0])
            graph_dot_y.append(city_list[vertex][1])
        plt.plot(graph_dot_x, graph_dot_y, '-o')
        plt.show()

    def solve_with_all_info(self, city_list):
        return self.__solve(city_list)

    def solve_with_list_and_cost(self, city_list):
        return self.__solve(city_list)[:2]

    def solve_with_cost_and_time(self, city_list):
        return self.__solve(city_list)[1:3]

    # 問題を解き、結果を最短経路のリストで表示する
    def solve_with_list(self, city_list):
        return self.__solve(city_list)[0]

    # 問題を解き、結果を最短経路のコストで表示する
    def solve_with_cost(self, city_list):
        return self.__solve(city_list)[1]

    def solve_with_time(self, city_list):
        return self.__solve(city_list)[2]

    def solve_with_other(self, city_list):
        return self.__solve(city_list)[3:]

    # 問題を解く
    def __solve(self, city_list):
        return self.solver.solve(city_list)

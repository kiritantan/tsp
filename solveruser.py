import matplotlib.pyplot as plt

from solver.annealing import Annealing
from solver.basesolver import BaseSolver
from solver.counting import Counting
from solver.double_opt import DoubleOpt
from solver.dynamicprogramming import DynamicProgramming
from solver.hillclimbing import HillClimbing
from solvername import SolverName


class SolverUser():
    def __init__(self, solver=SolverName.BaseSolver):
        if solver.name == "Counting":
            self.solver = Counting()
        elif solver.name == "DynamicProgramming":
            self.solver = DynamicProgramming()
        elif solver.name == "Annealing":
            self.solver = Annealing()
        elif solver.name == "DoubleOpt":
            self.solver = DoubleOpt()
        elif solver.name == "HillClimbing":
            self.solver = HillClimbing();
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

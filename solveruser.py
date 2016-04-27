import sys
from basesolver import BaseSolver
from counting import Counting
from dynamicprogramming import DynamicProgramming


class SolverUser():
    def __init__(self, solver_name="BaseSolver"):
        if solver_name == "BaseSolver":
            self.solver = BaseSolver()
        elif solver_name == "Counting":
            self.solver = Counting()
        elif solver_name == "DynamicProgramming":
            self.solver = DynamicProgramming()
        else:
            print("such solver doesn'y exit!")
            sys.exit()


    # 問題を解き、結果を最短系で都市をつなげたグラフで表示する
    def solve_with_graph(self, city_list):
        pass

    # 問題を解き、結果を最短経路のリストで表示する
    def solve_with_list(self, city_list):
        return self.__solve(city_list)

    # 問題を解き、結果を最短経路のコストで表示する
    def solve_with_cost(self, city_list):
        pass

    # 問題を解く
    def __solve(self, city_list):
        return self.solver.solve(city_list)

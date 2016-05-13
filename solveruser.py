from basesolver import BaseSolver
from counting import Counting
from dynamicprogramming import DynamicProgramming
from annealing import Annealing

class SolverUser():
    def __init__(self, solver_name="BaseSolver"):
        if solver_name == "Counting":
            self.solver = Counting()
        elif solver_name == "DynamicProgramming":
            self.solver = DynamicProgramming()
        elif solver_name == "Annealing":
            self.solver = Annealing()
        else:
            self.solver = BaseSolver()


    # 問題を解き、結果を最短系で都市をつなげたグラフで表示する
    def solve_with_graph(self, city_list):
        pass

    def solver_with_list_and_cost(self, city_list):
        return self.__solve(city_list)

    # 問題を解き、結果を最短経路のリストで表示する
    def solve_with_list(self, city_list):
        return self.__solve(city_list)[0]

    # 問題を解き、結果を最短経路のコストで表示する
    def solve_with_cost(self, city_list):
        return self.__solve(city_list)[1]

    # 問題を解く
    def __solve(self, city_list):
        return self.solver.solve(city_list)


class SolverUser():
    def __init__(self, solver_name="hoge"):
        if solver_name == "hoge":
            self.solver = "hoge"

    # 問題を解き、結果を最短系で都市をつなげたグラフで表示する
    def solve_with_graph(self, city_list):
        pass

    # 問題を解き、結果を最短経路のリストで表示する
    def solve_with_list(self, city_list):
        pass

    # 問題を解き、結果を最短経路のコストで表示する
    def solve_with_cost(self, city_list):
        pass

    # 問題を解く
    def __solve(self, city_list):
        pass

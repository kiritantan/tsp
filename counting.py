from basesolver import BaseSolver
import itertools


class Counting(BaseSolver):

    def __init__(self):
        self.city_number_permutation = []
        super().__init__()

    def solve(self, city_list):
        start = self.start_time()
        self.calc_permutation(len(city_list))
        for elem in self.city_number_permutation:
            cost = self.cost_evaluate(elem, city_list)
            if self.max_cost > cost:
                # 変更を出力する
                #print("{0} -> {1}".format(self.max_cost, cost))
                self.max_cost = cost
                circuit = elem
        end = self.end_time(start)
        return (circuit, self.max_cost, end)

    # 同じ経路を逆周りするものも混じっていて(n-1)!になってるので、それを削って(n-1)!/2の計算量にしたい
    def calc_permutation(self, number_of_city=1):
        self.city_number_permutation = []
        city_number_list = [x for x in range(0, number_of_city)][1:]
        city_number_permutation = list(map(list, itertools.permutations(city_number_list)))
        for elem in city_number_permutation:
            elem.insert(0, 0)
            elem.append(0)
        self.city_number_permutation = city_number_permutation

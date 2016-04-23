from basesolver import BaseSolver
import itertools


class Counting(BaseSolver):

    def solve(self, city_list, isVisualized=False):
        return self.__calc_permutation(len(city_list))


    def __cost_evaluate(self):
        pass

    def __calc_permutation(self, number_of_city=1):
        city_number_list = [x for x in range(0, number_of_city)]
        print(list(map(list, itertools.permutations(city_number_list))))

        return list(map(list, itertools.permutations(city_number_list)))



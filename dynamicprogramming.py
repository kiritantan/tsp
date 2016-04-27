from basesolver import BaseSolver
import sys

#0を起点に路を返すようにする。
class DynamicProgramming(BaseSolver):

    def solve(self, city_list):
        city_size = len(city_list)
        SMAX = 1 << city_size
        city_cost_matrix = [[[sys.maxsize, 0] for _ in range(SMAX)] for _ in range(city_size)]

        for i in range(city_size-1):
            city_cost_matrix[i][1 << i][0] = super().disc(city_list[i], city_list[city_size-1])
            city_cost_matrix[i][1 << i][1] = city_size - 1

        for s in range(1, SMAX):
            for i in range(city_size):
                if not ((1 << i) & s): continue
                for j in range(city_size):
                    if ((1 << j) & s): continue
                    tmp = city_cost_matrix[i][s][0] + super().disc(city_list[i], city_list[j])
                    if tmp < city_cost_matrix[j][s | (1 << j)][0]:
                        city_cost_matrix[j][s | (1 << j)][0] = tmp
                        city_cost_matrix[j][s | (1 << j)][1] = i

        return (self.get_route(city_cost_matrix, city_size, city_size - 1), city_cost_matrix[city_size - 1][SMAX - 1][0])

    def get_route(self, city_cost_matrix, city_number, start):
        route = [start]
        v = (1 << city_number) - 1
        p = start

        while len(route) < city_number:
            q = city_cost_matrix[p][v][1]
            route.append(q)
            v ^= (1 << p)
            p = q

        route.append(start)

        return route


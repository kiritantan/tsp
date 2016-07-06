from mst.basemst import BaseMst
import sys


class Prim(BaseMst):

    def create_mst(self, city_list, route_cost_matrix):
        city_number = len(city_list)
        v_set = [i for i in range(city_number)]
        v_including = [0]
        e_including = []
        while (len(v_including) < len(v_set)):
            minimum_cost_route = (sys.maxsize, (0, 0))
            for i in v_including:
                v_not_including = list(set(v_set) - set(v_including))
                for j in v_not_including:
                    if route_cost_matrix[i][j] < minimum_cost_route[0]:
                        minimum_cost_route = (route_cost_matrix[i][j], (i, j))
            v_including.append(minimum_cost_route[1][1])
            e_including.append(minimum_cost_route[1])
        return e_including

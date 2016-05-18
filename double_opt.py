from basesolver import BaseSolver
import sys


class DoubleOpt(BaseSolver):

    def solve(self, city_list):
        route_cost_matrix = (self.create_rout_cost_matrix(city_list))
        mst = self.create_mst(city_list, route_cost_matrix)
        euler_route = self.create_euler_route(mst)
        shortcut_euler_route = self.create_shortcut_euler_route(euler_route)
        return (shortcut_euler_route, self.cost_evaluate(shortcut_euler_route, city_list))

    def create_shortcut_euler_route(self, euler_route):
        return sorted(set(euler_route), key = euler_route.index) + [0]

    def create_euler_route(self, mst):
        euler_route = [0]
        euler_route.extend(self.__rec_create_euler_route(mst, 0))
        return euler_route

    def __rec_create_euler_route(self, mst, city):
        city_edges = [edge for edge in mst if edge[0] == city]
        if len(city_edges) == 0:
            return []
        city_not_edges = mst
        for edge in city_edges:
            city_not_edges = list(filter(lambda n: n != edge, city_not_edges))
        eulor_route = []
        for edge in city_edges:
            eulor_route.append(edge[1])
            eulor_route.extend(self.__rec_create_euler_route(city_not_edges, edge[1]))
            eulor_route.append(edge[0])
        return eulor_route

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

    def create_rout_cost_matrix(self, city_list):
        city_number = len(city_list)
        route_cost_matrix = [[0 for _ in range(city_number)] for _ in range(city_number)]
        for src_city_coordinate in range(city_number):
            for dist_city_coodinate in range(city_number):
                route_cost_matrix[src_city_coordinate][dist_city_coodinate] = self.disc(city_list[src_city_coordinate],\
                                                                                        city_list[dist_city_coodinate])
        return route_cost_matrix

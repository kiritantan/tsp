from mst.basemst import BaseMst
from mst.prim import Prim
from solver.basesolver import BaseSolver
from mstname import MstName


class DoubleOpt(BaseSolver):

    def solve(self, city_list):
        mst_algorithm = MstName.Prim
        start = self.start_time()
        route_cost_matrix = (self.create_rout_cost_matrix(city_list))
        mst = self.create_mst(city_list, route_cost_matrix, mst_algorithm)
        euler_route = self.create_euler_route(mst)
        shortcut_euler_route = self.create_shortcut_euler_route(euler_route)
        end = self.end_time(start)
        return (shortcut_euler_route, self.cost_evaluate(shortcut_euler_route, city_list), end)

    def create_shortcut_euler_route(self, euler_route):
        return sorted(set(euler_route), key=euler_route.index) + [0]

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

    def create_mst(self, city_list, route_cost_matrix, mst_algorithm=MstName.BaseMst):
        if mst_algorithm.name == 'Prim':
            return Prim().create_mst(city_list, route_cost_matrix)
        else:
            return BaseMst().create_mst(city_list, route_cost_matrix)

    def create_rout_cost_matrix(self, city_list):
        city_number = len(city_list)
        route_cost_matrix = [[0 for _ in range(city_number)] for _ in range(city_number)]
        for src_city_coordinate in range(city_number):
            for dist_city_coodinate in range(city_number):
                route_cost_matrix[src_city_coordinate][dist_city_coodinate] = self.disc(city_list[src_city_coordinate],\
                                                                                        city_list[dist_city_coodinate])
        return route_cost_matrix

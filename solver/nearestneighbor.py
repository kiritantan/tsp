from solver.basesolver import BaseSolver


class NearestNeighbor(BaseSolver):

    def solve(self, city_list):
        start = self.start_time()
        initial_city = 0
        city_number = len(city_list)
        current_city = initial_city
        cost_matrix = self.create_cost_matrix(city_list)
        route = [current_city]
        available_cities = [i for i in range(city_number)]
        available_cities.remove(initial_city)
        while available_cities != []:
            nearest_neighbor = available_cities[0]
            for dist in available_cities:
                if cost_matrix[current_city][nearest_neighbor] > cost_matrix[current_city][dist]:
                    nearest_neighbor = dist

            route.append(nearest_neighbor)
            available_cities.remove(nearest_neighbor)
            current_city = nearest_neighbor
        route.append(initial_city)
        cost = self.cost_evaluate(route, city_list)
        end = self.end_time(start)
        return (route, cost, end)

    def create_cost_matrix(self, city_list):
        city_number = len(city_list)
        route_cost_matrix = [[0 for _ in range(city_number)] for _ in range(city_number)]
        for src_city_coordinate in range(city_number):
            for dist_city_coodinate in range(city_number):
                route_cost_matrix[src_city_coordinate][dist_city_coodinate] = self.disc(city_list[src_city_coordinate], \
                                                                                    city_list[dist_city_coodinate])
        return route_cost_matrix
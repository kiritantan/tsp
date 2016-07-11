from solver.basesolver import BaseSolver


class NearestInsertion(BaseSolver):

    def solve(self, city_list):
        start = self.start_time()
        initial_city = 0
        city_number = len(city_list)
        current_city = initial_city
        cost_matrix = self.create_cost_matrix(city_list)
        route = [current_city, current_city]
        available_cities = [i for i in range(city_number)]
        available_cities.remove(initial_city)
        while len(route) < len(city_list):
            nearest_city = -1
            nearest_insert_index = -1
            for index in range(len(route[:-1])):
                source = route[index]
                nearest_city_at_source = available_cities[0]
                for dist in available_cities[1:]:
                    if cost_matrix[source][nearest_city_at_source] > cost_matrix[source][dist]:
                        nearest_city_at_source = dist
                if nearest_city == -1:
                    nearest_city = nearest_city_at_source
                    nearest_insert_index = index
                else:
                    if cost_matrix[source][nearest_city] > cost_matrix[source][nearest_city_at_source]:
                        nearest_city = nearest_city_at_source
                        nearest_insert_index = index

            route = route[:nearest_insert_index+1] + [nearest_city] + route[nearest_insert_index+1:]
            available_cities.remove(nearest_city)
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
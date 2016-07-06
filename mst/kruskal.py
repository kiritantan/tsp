from mst.basemst import BaseMst


class Kruskal(BaseMst):

    group = 0
    group_set =
    def create_mst(self, city_list, route_cost_matrix):


class Edge:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight
from mst.basemst import BaseMst
from mst.pqueue import *

class Kruskal(BaseMst):

    def create_mst(self, city_list, route_cost_matrix):
        NODE_SIZE = len(city_list)
        group = [i for i in range(NODE_SIZE)]
        group_set = [set([i]) for i in range(NODE_SIZE)]
        edges = self.make_edge(NODE_SIZE, route_cost_matrix)
        e_including = []
        i = 0
        while i < NODE_SIZE - 1:
           e = edges.pop()
           if group[e.p1] != group[e.p2]:
               self.merge(e.p1, e.p2, group, group_set)
               e_including.append((e.p1, e.p2))
               i += 1
        sorted_e_including = self.__sort_edge_set(NODE_SIZE, e_including)
        return sorted_e_including


    def make_edge(self, node_size, edge_data):
        edges = PQueue()
        for i in range(node_size):
            for j in range(node_size):
                e = Edge(i, j, edge_data[i][j])
                edges.push(e)
        return edges

    def merge(self, node1, node2, group, group_set):
        gs1 = group_set[group[node1]]
        gs2 = group_set[group[node2]]
        if len(gs1) <= len(gs2):
            gs1.update(gs2)
            gs3 = gs2
            g = group[node1]
        else:
            gs2.update(gs1)
            gs3 = gs1
            g = group[node2]
        for x in gs3:
            group[x] = g
        gs3.clear()

    def __sort_edge_set(self, node_size, e_set):
        used_v_set = []
        new_uesd_v_set = [0]
        while (len(used_v_set) < node_size):
            used_v_set.extend(new_uesd_v_set)
            now_used_v_set = new_uesd_v_set
            new_uesd_v_set = []
            for v in now_used_v_set:
                for index in range(len(e_set)):
                    edge = e_set[index]
                    if edge[0] == v:
                        new_uesd_v_set.append(edge[1])
                    elif edge[1] == v:
                        flag = True
                        for used_v in used_v_set:
                            if edge[0] == used_v:
                                flag = False
                        if flag:
                            e_set[index] = (edge[1], edge[0])
                            new_uesd_v_set.append(edge[0])
        return e_set

class Edge(object):
    def __init__(self, p1, p2, weight):
        self.p1 = p1
        self.p2 = p2
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

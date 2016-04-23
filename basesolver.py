from math import sqrt


class BaseSolver(object):

    def solve(self, city_list, isVisualized=False):
        raise Exception("plese set solve algorithm")

    def __create_matrix(self, city_list):
        dist_matrix = []
        for i in range(0, len(city_list)):
            dist_list = []
            for j in range(0, len(city_list)):
                dist_list.append(self.__disc(city_list[i],city_list[j]))
            dist_matrix.append(dist_list)
        return dist_matrix

    def __disc(self, city1, city2):
        dx = city1[0]-city2[0]
        dy = city1[1]-city2[1]
        return int(sqrt(dx**2+dy**2)+0.5)

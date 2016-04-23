from math import sqrt


class BaseSolver(object):
    def solve(self,city_list=[],isVisualized=False):
        raise Exception("plese set solve algorithm")

    def disc(self, city1, city2):
        dx = city1[0]-city2[0]
        dy = city1[1]-city2[1]
        return int(sqrt(dx**2+dx**2)+0.5)

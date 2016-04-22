
class BaseSolver(object):
    def solve(self,city_list=[]):
        raise Exception("plese set solve algorithm")

if __name__ == "__main__":
    b = BaseSolver()
    b.solve()

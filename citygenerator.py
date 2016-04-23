import random


class CityGenerator():
    def generate(self, name='city') -> object:
        self.file_name = name + ".ssv"
        random.seed(1)
        city_dict = {}
        loop_number = 20
        f = open(self.file_name, 'w')
        while len(city_dict) < loop_number:
            x = round(random.random() * (10 ** 5), 4)
            y = round(random.random() * (10 ** 5), 4)
            if not "{0},{1}".format(x, y) in city_dict:
                f.write("{0} {1} {2}\n".format(len(city_dict), x, y))
                city_dict["{0},{1}".format(x, y)] = True
        f.close()

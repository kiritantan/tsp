import random


class CityGenerator():
    def generate(self, name='city', city_number=10, city_size=1000, random_seed=0):
        self.file_name = name + '.ssv'
        if random_seed != 0:
            random.seed(random_seed)
        city_dict = {}
        f = open(self.file_name, 'w')
        while len(city_dict) < city_number:
            x = round(random.random() * (city_size), 0)
            y = round(random.random() * (city_size), 0)
            if not "{0},{1}".format(x, y) in city_dict:
                f.write("{0} {1} {2}\n".format(len(city_dict), x, y))
                city_dict["{0},{1}".format(x, y)] = True
        f.close()
        random.seed()

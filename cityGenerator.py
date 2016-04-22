import random

if __name__ == "__main__":
    random.seed(1)
    city_dict = {}
    loop_number = 1000
    while len(city_dict) < loop_number:
        x = round(random.random() * (10**5),4)
        y = round(random.random() * (10**5),4)
        if not "{0},{1}".format(x,y) in city_dict :
            print("{0} {1} {2}".format(len(city_dict),x, y))
            city_dict["{0},{1}".format(x,y)] = True

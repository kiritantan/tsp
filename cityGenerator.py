import random

if __name__ == "__main__":
    city_dict = {}
    count = 0
    while len(city_dict) < 100:
        x = random.randrange(100)
        y = random.randrange(100)
        if not "{0},{1}".format(x,y) in city_dict :
            print("{0},{1}".format(x, y))
            city_dict["{0},{1}".format(x,y)] = True
        count += 1

    print(count)

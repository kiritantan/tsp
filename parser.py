import re

class Parser():
    def parse(self,file_name="city"):
        file = open(file_name+".ssv")
        lines = file.readlines()
        city_coordinates = []
        pattern = r'[ ]+'
        repatter = re.compile(pattern)
        for line in lines:
            re_line = re.split(repatter, line)
            fi_line = list(filter(lambda s: s != '', re_line))[1:]
            coordinates = [float(x) for x in fi_line]
            city_coordinates.append(coordinates)
        return city_coordinates


class Parser():
    def parse(self,file_name="city"):
        file = open(file_name+".ssv")
        lines = file.readlines()
        city_coordinates = []
        for line in lines:
            list = line.strip().split(" ")[1:]
            coordinates = [float(x) for x in list]
            city_coordinates.append(coordinates)
        return city_coordinates

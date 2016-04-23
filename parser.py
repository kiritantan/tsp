
class Parser():
    def parse(self,file_name="city"):
        file = open(file_name+".ssv")
        lines = file.readlines()
        city_coodinates = []
        for line in lines:
            coodinates = line.strip().split(" ")[1:]
            city_coodinates.append(coodinates)

        return city_coodinates

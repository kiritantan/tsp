
from citygenerator import CityGenerator
from parser import  Parser
from solveruser import SolverUser

if __name__ == "__main__":
    file_name = "city"
    generator = CityGenerator()
    generator.generate(file_name)
    parser = Parser()
    city_list = parser.parse(file_name)
    user = SolverUser()
    user.solve_with_list(city_list)


from citygenerator import CityGenerator
from parser import  Parser
from solveruser import SolverUser

if __name__ == "__main__":
    file_name = "city"
    city_number = 10
    generator = CityGenerator()
    generator.generate(file_name, city_number)
    parser = Parser()
    city_list = parser.parse(file_name)
    user_counting = SolverUser("Counting")
    print(user_counting.solve_with_list(city_list))
    user_dynamicprogramming = SolverUser("DynamicProgramming")
    print(user_dynamicprogramming.solve_with_list(city_list))
from citygenerator import CityGenerator
from parser import  Parser
from solveruser import SolverUser


def hukusuu_tsp(loop_num, city_number, city_size, solver_name):
    generator = CityGenerator()
    parser = Parser()
    user = SolverUser(solver_name)
    for _ in range(loop_num):
        generator.generate(file_name, city_number, city_size)
        city_list = parser.parse(file_name)
        print(user.solve_with_cost(city_list))

if __name__ == "__main__":
    file_name = "city"
    tsp_file_name = "a280"
    city_number = 10
    city_size = 10000
    solver_name_list = ["Counting", "DynamicProgramming", "Annealing", "DoubleOpt", "HillClimbing"]
    generator = CityGenerator()
    generator.generate(file_name, city_number, city_size, 1)
    parser = Parser()
    city_list = parser.parse(file_name)
    for index in [2, 4]:
        user_counting = SolverUser(solver_name_list[index])
        print(solver_name_list[index])
        print(user_counting.solve_with_list_and_cost(city_list))
        #user_counting.solve_with_graph(city_list)
    #hukusuu_tsp(10, city_number, city_size, 'DoubleOpt')

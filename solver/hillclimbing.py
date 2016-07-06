from solver.basesolver import BaseSolver


class HillClimbing(BaseSolver):
    def __init__(self):
        self.neighboor = []
        self.size = 5
        super().__init__()

    # 適当な構築法を使っていい感じの巡回路を作るのもよし、適当にするもよし
    def solve(self, city_list):
        start = self.start_time()
        self.circuit = [i for i in range(len(city_list))]
        self.store_neighboor(city_list)
        circuit = self.climbing(self.circuit, city_list)
        end = self.end_time(start)
        return (circuit, self.cost_evaluate(circuit, city_list), end)

    def climbing(self, circuit, city_list):
        city_num = len(city_list)
        for _ in range(self.size):
            for i in range(city_num):
                a = circuit[i]
                b = self.next_city(a, circuit)
                for c in self.neighboor[i]:
                    if b == c:
                        continue
                    d = self.next_city(c, circuit)
                    if b == d or a == d:
                        continue
                    tmp = self.disc(city_list[a], city_list[b]) + self.disc(city_list[c], city_list[d]) - \
                          self.disc(city_list[a], city_list[c]) - self.disc(city_list[b], city_list[d])
                    if tmp >= 0:
                        self.flip_cities(b, c, circuit)
        circuit = self.sort_circuit(circuit)
        circuit.append(0)
        return circuit

    def store_neighboor(self, city_list):
        neighboor_num = 10
        city_num = len(city_list)
        for i in range(city_num):
            provisional_neighboor = []
            for j in range(city_num):
                if i == j:
                    continue
                for (num, k) in enumerate(provisional_neighboor):
                    if self.disc(city_list[i], city_list[k]) > self.disc(city_list[i], city_list[j]):
                        provisional_neighboor.insert(num, j)
                        break
                if j not in provisional_neighboor:
                    provisional_neighboor.append(j)
            self.neighboor.append(provisional_neighboor[:neighboor_num - 1])

    def next_city(self, i, circuit):
        return circuit[(circuit.index(i) + 1) % len(circuit)]

    def flip_cities(self, b, c, circuit):
        b_index = circuit.index(b)
        c_index = circuit.index(c)
        circuit[b_index] = c
        circuit[c_index] = b
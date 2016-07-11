import random
import math
from solver.basesolver import BaseSolver
from solver.nearestneighbor import NearestNeighbor

class FireFlySystem(BaseSolver):

    def __init__(self):
        super().__init__()
        self.FIREFLY_NUMBER = 20
        self.MAX_ITER = 100
        self.GANMA = 0.07
        self.DESCENDANTS_NUMBER = 8

    def solve(self, city_list):
        start = self.start_time()
        current_generation = self.create_initial_firefly(self.FIREFLY_NUMBER, city_list)
        current_generation = self.select_brightst_fireflies(current_generation)
        next_generation = []
        best_firefly = current_generation[0]
        for _ in range(self.MAX_ITER):
            next_generation.append(best_firefly)
            for firefly in current_generation:
                attractive_firefly = self.find_attractive_firefly(firefly, current_generation)
                if attractive_firefly is firefly:
                    for _ in range(self.DESCENDANTS_NUMBER):
                        next_generation.append(firefly.move_randomly(city_list))
                else:
                    for _ in range(self.DESCENDANTS_NUMBER):
                        next_generation.append(firefly.move_like_attracted(attractive_firefly, city_list))
            current_generation = self.select_brightst_fireflies(next_generation)
            next_generation = []
            best_firefly = current_generation[0]
        end = self.end_time(start)
        return (best_firefly.gene, int(1 / best_firefly.brightness), end)

    def find_attractive_firefly(self, f1, fireflies):
        best_firefly = f1
        best_attractiveness = f1.brightness
        for firefly in fireflies:
            attractiveness = firefly.brightness * math.pow(math.e, -self.GANMA * math.pow(f1.calc_firefly_dist(firefly), 2))
            if best_attractiveness < attractiveness:
                best_firefly = firefly
                best_attractiveness = attractiveness
        return best_firefly

    def create_initial_firefly(self, firefly_num, city_list):
        gene = NearestNeighbor().solve(city_list)[0]
        mutate_gene = [i for i in gene]
        random.shuffle(mutate_gene)
        fireflies = []
        for _ in range(firefly_num):
            rand = random.random()
            if rand > 0.8:
                new_gene = self.mutate_gene(gene, city_list)
                brightness = 1 / self.cost_evaluate(new_gene, city_list)
                fireflies.append(FireFly(new_gene, brightness))
            else:
                brightness = 1 / self.cost_evaluate(mutate_gene, city_list)
                fireflies.append(FireFly(mutate_gene, brightness))
                random.shuffle(mutate_gene)
        return fireflies

    def mutate_gene(self, gene, city_list):
        gene = [i for i in gene[:-1]]
        permutation_length = random.randint(2, 10)
        m = random.randrange(len(city_list) - permutation_length)
        mutate_gene = gene[:m] + list(reversed(gene[m:m + permutation_length])) + gene[m + permutation_length:]
        mutate_gene.append(mutate_gene[0])
        return mutate_gene

    def select_brightst_fireflies(self, fireflies):
        return sorted(fireflies, key=lambda x: x.brightness, reverse=True)[:self.FIREFLY_NUMBER]

class FireFly(object):

    def __init__(self, gene, brightness):
        super().__init__()
        self.gene = gene
        self.brightness = brightness

    def calc_move_dist(self, other):
        dist = int(self.calc_firefly_dist(other))
        if dist <= 2:
            return 2
        else:
            return random.randint(2, dist)

    def calc_firefly_dist(self, other):
        arc = 0
        for index in range(len(self.gene)):
            if self.gene[index] != other.gene[index]:
                arc += 1
        return (arc / len(self.gene)) * 10

    def move_like_attracted(self, other, city_list):
        new_gene = [i for i in self.gene[:-1]]
        permutation_length = self.calc_move_dist(other)
        m = random.randrange(len(city_list) - permutation_length)
        new_gene = new_gene[:m] + list(reversed(new_gene[m:m+permutation_length])) + new_gene[m+permutation_length:]
        new_gene.append(new_gene[0])
        brightness = 1 / self.cost_evaluate(new_gene, city_list)
        return FireFly(new_gene, brightness)

    def move_randomly(self, city_list):
        new_gene = [i for i in self.gene[:-1]]
        permutation_length = random.randint(2, 10)
        m = random.randrange(len(city_list) - permutation_length)
        new_gene = new_gene[:m] + list(reversed(new_gene[m:m+permutation_length])) + new_gene[m+permutation_length:]
        new_gene.append(new_gene[0])
        brightness = 1 / self.cost_evaluate(new_gene, city_list)
        return FireFly(new_gene, brightness)

    def disc(self, city1: object, city2: object) -> object:
        dx = city1[0] - city2[0]
        dy = city1[1] - city2[1]
        return int(math.sqrt(dx ** 2 + dy ** 2) + 0.5)

    def cost_evaluate(self, circuit, city_list):
        sum = 0
        city_num = len(circuit)
        for index in range(city_num):
            sum += self.disc(city_list[circuit[index]], city_list[circuit[(index + 1) % city_num]])
        return sum
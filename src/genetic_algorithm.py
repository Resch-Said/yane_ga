from population import Population


class GeneticAlgorithm:
    def __init__(self):
        self.fitness_function = None
        self.solution = [1, 2, 3, 4, 5, 6]
        self.population: list[Population] = []
        self.population_size = 0
        self.max_generations = 0

    def set_fitness_function(self, fitness_function):
        self.fitness_function = fitness_function

    def add_population(self, population):
        self.population.append(population)

    def remove_population(self, population):
        self.population.remove(population)

    def set_population_size(self, size):
        self.population_size = size

    def set_max_generations(self, max_generations):
        self.max_generations = max_generations

    def run(self):
        self.initialize_population()
        for i in range(self.max_generations):
            self.evaluate_population()
            self.crossover()
            self.mutate()
            self.select_survivors()

    def initialize_population(self):
        for i in range(self.population_size):
            population = Population()
            population.initialize(len(self.solution))
            self.population.append(population.copy())

    def evaluate_population(self):
        for pop in self.population:
            pop.evaluate(self.fitness_function)

    def select_parents(self):
        pass

    def crossover(self):
        pass

    def mutate(self):
        for pop in self.population:
            pop.mutate()

    def select_survivors(self):
        pass

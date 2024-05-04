import math

from chromosome import Chromosome
import random

from config import Config
from utils.crossover_util import CrossoverUtil


class Population:
    def __init__(self, length=None, genes_length=None):
        self.chromosomes: list[Chromosome] = []

        if length and genes_length:
            self.initialize(length, genes_length)

    def initialize(self, length, genes_length):
        for _ in range(length):
            chromo = Chromosome().initialize(genes_length)
            self.add_chromosome(chromo)

    def add_chromosome(self, values):
        if isinstance(values, Chromosome):
            self.chromosomes.append(values)
        elif isinstance(values, list):
            chromo = Chromosome()
            self.chromosomes.append(chromo.set_genes(values))

    def remove_chromosome(self, chromosome: Chromosome):
        self.chromosomes.remove(chromosome)

    def mutate(self, mutation_rate=Config.get_gene_mutation_rate()):
        for chromo in self.chromosomes:
            chromo.mutate(mutation_rate=mutation_rate)

    def crossover(self, chromosome1, chromosome2):
        genes1 = chromosome1.get_genes()
        genes2 = chromosome2.get_genes()

        child_genes = CrossoverUtil.crossover(genes1, genes2)
        self.add_chromosome(Chromosome().set_genes(child_genes))

    def evaluate(self, fitness_function):
        for chromo in self.chromosomes:
            chromo.evaluate(fitness_function)

    def copy(self):
        pop = Population()
        for chromo in self.chromosomes:
            pop.add_chromosome(chromo.copy())
        return pop

    def get_length(self):
        return len(self.chromosomes)

    def tournament_selection(self, k=None):
        if k is None:
            k = math.ceil(self.get_length() * Config.get_tournament_selection_k())
        selected = []
        for _ in range(k):
            selected.append(random.choice(self.chromosomes))
        return max(selected, key=lambda chromo: chromo.fitness)


if __name__ == "__main__":
    population = Population()

    population.add_chromosome([1, 2, 3, 4])
    population.add_chromosome([5, 6])
    for chromo in population.chromosomes:
        print(chromo)

    population.crossover(population.chromosomes[0], population.chromosomes[1])

    for chromo in population.chromosomes:
        print(chromo)

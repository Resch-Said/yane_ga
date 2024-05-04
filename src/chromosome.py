from config import Config
from gene import Gene
import random


class Chromosome:
    def __init__(self, gene_length=None):
        self.genes: list[Gene] = []
        self.fitness = None

        if gene_length:
            self.initialize(gene_length)

    def initialize(self, length):
        for _ in range(length):
            self.add_gene(Gene(initialize=True))
        return self

    def add_gene(self, gene: Gene):
        self.genes.append(gene)

    def remove_gene(self, gene: Gene):
        self.genes.remove(gene)

    def get_genes(self):
        return self.genes

    def get_gene_values(self):
        return [gene.get_value() for gene in self.genes]

    def get_length(self):
        return len(self.genes)

    def copy(self) -> "Chromosome":
        chromo = Chromosome()
        for gene in self.genes:
            chromo.add_gene(gene.copy())
        return chromo

    def mutate(self, mutation_rate=Config.get_gene_mutation_rate()):
        for gene in self.genes:
            gene.mutate(mutation_rate=mutation_rate)

    def __str__(self):
        return str([str(gene) for gene in self.genes])

    def set_genes(self, values):

        for value in values:
            self.add_gene(Gene().set_value(value))
        return self

    def evaluate(self, fitness_function):
        self.fitness = fitness_function(self.get_gene_values())
        return self.fitness


if __name__ == "__main__":
    pass

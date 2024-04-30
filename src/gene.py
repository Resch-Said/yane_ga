import random

from config import Config


class Gene:
    def __init__(self):
        self.value = 0

    def mutate(self, min=0, max=1, mutation_rate=Config.get_gene_mutation_rate()):
        if random.random() < mutation_rate:
            self.value = random.uniform(min, max)

    def __str__(self):
        return str(self.value)

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

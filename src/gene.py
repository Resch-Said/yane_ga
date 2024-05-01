import random

from config import Config


class Gene:
    def __init__(self, value=None, initialize=False):
        self.value = value

        if initialize:
            self.initialize()

    def mutate(
        self,
        min=Config.get_min_value(),
        max=Config.get_max_value(),
        use_value_pool=False,
        mutation_rate=Config.get_gene_mutation_rate(),
    ):
        if random.random() < mutation_rate:
            if use_value_pool:
                value_pool = Config.get_value_pool()
                value_pool.append(random.uniform(min, max))
                self.value = random.choice(value_pool)
            else:
                self.value = random.uniform(min, max)

    def __str__(self):
        return str(self.value)

    def set_value(self, value):
        self.value = value
        return self

    def get_value(self):
        return self.value

    def copy(self) -> "Gene":
        gene = Gene()
        gene.set_value(self.get_value())
        return gene

    def initialize(self, use_value_pool=False):
        self.mutate(use_value_pool=use_value_pool, mutation_rate=1)

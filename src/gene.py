import random

from config import Config

# TODO: Allow to add custom gene types like objects, strings, etc.


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
            random_value = random.uniform(min, max)
            value_pool = [random_value]

            try:
                value_shift_down = self.value * 0.9
                value_shift_up = self.value * 1.1
                value_pool.extend([value_shift_down, value_shift_up])
            except TypeError:
                pass

            if use_value_pool:
                value_pool.extend(Config.get_value_pool())

            # We can later use random.choices() to change the probability of each value being selected,
            # if we start to automatically adjust parameters.
            # Maybe we can use a dictionary to store the values and their probabilities.
            self.value = random.choice(value_pool)

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

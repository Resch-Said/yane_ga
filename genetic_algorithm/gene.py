from copy import deepcopy
import random

from custom_gene import CustomGene


class Gene:
    def __init__(self, value=None):
        self.value = value
        self.value_pool = []

    def copy(self):
        if isinstance(self.value, (int, str, float)):
            return Gene(self.value)

        return deepcopy(self)

    def mutate_random(self, min_value=0, max_value=1):
        self.value = random.uniform(min_value, max_value)

    def mutate_pool(self):
        self.value = random.choice(self.value_pool)

    def mutate(self, min_value=None, max_value=None):
        if isinstance(self.value, CustomGene):
            self.value.mutate()

        mutation_function = []

        if min_value is not None and max_value is not None:
            mutation_function.append(self.mutate_random)
        if self.value_pool:
            mutation_function.append(self.mutate_pool)

        if mutation_function:
            mutation_function = random.choice(mutation_function)
        else:
            mutation_function = None

        if mutation_function == self.mutate_random:
            mutation_function(min_value, max_value)
        elif mutation_function == self.mutate_pool:
            mutation_function()

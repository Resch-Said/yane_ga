from itertools import zip_longest
import random


class CrossoverUtil:
    @classmethod
    def crossover(cls, parent1, parent2):
        child = []
        for gene1, gene2 in zip_longest(parent1, parent2):
            random_gene = gene1 if bool(random.getrandbits(1)) else gene2
            if random_gene is not None:
                child.append(random_gene)
        return child


if __name__ == "__main__":
    a = ["1", "2", "3", "4"]
    b = ["1", "2"]
    print(CrossoverUtil.crossover(a, b))

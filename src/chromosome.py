from gene import Gene


class Chromosome:
    def __init__(self):
        self.genes: list[Gene] = []

    def add_gene(self, gene: Gene):
        self.genes.append(gene)

    def remove_gene(self, gene: Gene):
        self.genes.remove(gene)

    def remove_gene_at(self, index: int):
        self.genes.pop(index)

    def get_gene_at(self, index: int):
        return self.genes[index]

    def get_genes(self):
        return self.genes

    def get_genes_between(self, start: int, end: int):
        return self.genes[start : end + 1]

    def get_gene_values(self):
        return [gene.get_value() for gene in self.genes]

    def get_length(self):
        return len(self.genes)

    def copy(self):
        chromo = Chromosome()
        for gene in self.genes:
            chromo.add_gene(gene.copy())
        return chromo

    def mutate(self):
        for gene in self.genes:
            gene.mutate()

    def __str__(self):
        return str([str(gene) for gene in self.genes])


if __name__ == "__main__":
    chromosome = Chromosome()
    gene = Gene()
    chromosome.add_gene(gene.copy())
    chromosome.add_gene(gene.copy())
    chromosome.add_gene(gene.copy())
    chromosome.add_gene(gene.copy())
    chromosome.add_gene(gene.copy())
    chromosome.add_gene(gene.copy())
    chromosome.add_gene(gene.copy())
    chromosome.add_gene(gene.copy())
    chromosome.add_gene(gene.copy())
    chromosome.add_gene(gene.copy())
    chromosome.mutate()
    print(chromosome)
    print(chromosome.get_gene_values())
    print(chromosome.get_length())
    print(chromosome.get_gene_at(0))
    print(chromosome.get_genes_between(0, 5))
    print(chromosome.get_genes())
    chromosome.remove_gene_at(0)
    print(chromosome)
    chromosome.remove_gene(chromosome.get_gene_at(0))
    print(chromosome)
    print(chromosome.get_genes_between(0, 1))

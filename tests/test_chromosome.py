import unittest
import random

from chromosome import Chromosome
from config import Config
from gene import Gene


class TestChromosome(unittest.TestCase):
    def setUp(self):
        self.chromosome = Chromosome()

    def test_initialize(self):
        self.chromosome.initialize(10)
        self.assertEqual(self.chromosome.get_length(), 10)
        self.assertEqual(Chromosome().initialize(10).get_length(), 10)
        self.assertTrue(None not in self.chromosome.get_gene_values())

    def test_add_gene(self):
        gene = Gene(initialize=True)
        self.chromosome.add_gene(gene)
        self.assertTrue(gene in self.chromosome.get_genes())

    def test_remove_gene(self):
        gene = Gene(initialize=True)
        self.chromosome.add_gene(gene)
        self.chromosome.remove_gene(gene)
        self.assertTrue(gene not in self.chromosome.get_genes())

    def test_get_genes(self):
        gene = Gene(initialize=True)
        self.chromosome.add_gene(gene)
        self.assertEqual(self.chromosome.get_genes(), [gene])

    def test_length(self):
        gene = Gene(initialize=True)
        self.chromosome.add_gene(gene)
        self.chromosome.add_gene(gene)
        self.assertEqual(self.chromosome.get_length(), 2)

    def test_copy(self):
        gene = Gene(initialize=True)
        self.chromosome.add_gene(gene)
        copy_chromosome = self.chromosome.copy()
        self.assertEqual(
            self.chromosome.get_gene_values(), copy_chromosome.get_gene_values()
        )
        self.assertNotEqual(self.chromosome, copy_chromosome)

    def test_get_gene_values(self):
        gene = Gene(2)
        self.chromosome.add_gene(gene)
        self.assertEqual(self.chromosome.get_gene_values(), [2])

    def test_mutate(self):
        random.seed(0)
        gene = Gene(2)
        self.chromosome.add_gene(gene)
        self.chromosome.mutate(mutation_rate=1)
        self.assertNotEqual(self.chromosome.get_gene_values(), [2])

    def test_set_genes(self):
        self.chromosome.set_genes([1, 2, 3])
        self.assertEqual(self.chromosome.get_gene_values(), [1, 2, 3])

    def test_evaluation(self):

        def fitness_function(solution):
            return sum(solution)

        gene = Gene(1)
        self.chromosome.add_gene(gene)
        self.chromosome.add_gene(gene)
        self.chromosome.evaluate(fitness_function)

        self.assertEqual(self.chromosome.fitness, 2)

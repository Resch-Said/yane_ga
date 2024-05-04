import unittest
import random

from chromosome import Chromosome
from config import Config
from gene import Gene
from population import Population


class TestPopulation(unittest.TestCase):
    def setUp(self):
        self.population = Population()

    def test_initialize(self):
        gene_length = 10
        population_length = 1

        self.population.initialize(population_length, genes_length=gene_length)
        self.assertEqual(self.population.get_length(), population_length)
        self.assertTrue(None not in self.population.chromosomes[0].get_gene_values())
        self.assertTrue(self.population.chromosomes[0].get_length() == gene_length)

    def test_add_chromosome(self):
        gene_length = 10
        chromosome = Chromosome().initialize(gene_length)
        self.population.add_chromosome(chromosome)
        self.assertEqual(self.population.get_length(), 1)
        self.assertEqual(self.population.chromosomes[0], chromosome)
        self.assertEqual(self.population.chromosomes[0].get_length(), gene_length)

    def test_remove_chromosome(self):
        gene_length = 10
        chromosome = Chromosome().initialize(gene_length)
        self.population.add_chromosome(chromosome)
        self.population.remove_chromosome(chromosome)
        self.assertEqual(self.population.get_length(), 0)
        self.assertEqual(self.population.chromosomes, [])

    def test_mutate(self):
        gene_length = 3
        random.seed(1)

        chromosome = Chromosome().initialize(gene_length)
        self.population.add_chromosome(chromosome)

        original_values = chromosome.get_gene_values()

        self.population.mutate(mutation_rate=1)
        self.assertTrue(None not in self.population.chromosomes[0].get_gene_values())
        self.assertTrue(
            original_values != self.population.chromosomes[0].get_gene_values()
        )

    def test_crossover_equal_gene_length(self):
        gene_length = 3
        chromosome1 = Chromosome().initialize(gene_length)
        chromosome2 = Chromosome().initialize(gene_length)

        self.population.add_chromosome(chromosome1)
        self.population.add_chromosome(chromosome2)

        self.population.crossover(chromosome1, chromosome2)

        self.assertEqual(self.population.get_length(), 3)
        self.assertTrue(None not in self.population.chromosomes[2].get_gene_values())
        self.assertTrue(self.population.chromosomes[2].get_length() == gene_length)

    def test_crossover_different_gene_length(self):
        gene_length1 = 3
        gene_length2 = 4
        chromosome1 = Chromosome().initialize(gene_length1)
        chromosome2 = Chromosome().initialize(gene_length2)

        self.population.add_chromosome(chromosome1)
        self.population.add_chromosome(chromosome2)

        self.population.crossover(chromosome1, chromosome2)

        self.assertEqual(self.population.get_length(), 3)
        self.assertTrue(None not in self.population.chromosomes[2].get_gene_values())

    def test_copy(self):
        gene_length = 3
        chromosome = Chromosome().initialize(gene_length)
        self.population.add_chromosome(chromosome)

        copied_population = self.population.copy()
        self.assertEqual(self.population.get_length(), copied_population.get_length())
        self.assertEqual(
            self.population.chromosomes[0].get_gene_values(),
            copied_population.chromosomes[0].get_gene_values(),
        )
        self.assertNotEqual(
            id(self.population.chromosomes[0]), id(copied_population.chromosomes[0])
        )
        self.assertNotEqual(self.population, copied_population)

    def test_evaluate(self):
        gene_length = 3
        chromosome = Chromosome().initialize(gene_length)
        self.population.add_chromosome(chromosome)

        expected_fitness = sum(chromosome.get_gene_values())

        def fitness_function(values):
            return sum(values)

        self.population.evaluate(fitness_function)
        self.assertTrue(self.population.chromosomes[0].fitness is not None)
        self.assertEqual(self.population.chromosomes[0].fitness, expected_fitness)

    def test_get_length(self):
        gene_length = 3
        chromosome = Chromosome().initialize(gene_length)
        self.population.add_chromosome(chromosome)

        self.assertEqual(self.population.get_length(), 1)

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

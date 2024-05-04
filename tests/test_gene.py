import unittest
import random

from config import Config
from gene import Gene


class TestGene(unittest.TestCase):
    def test_gene(self):
        gene = Gene("A")
        self.assertEqual(gene.value, "A")

    def test_gene_number(self):
        gene = Gene(2)
        self.assertEqual(gene.value, 2)

    def test_gene_empty(self):
        gene = Gene()
        self.assertEqual(gene.value, None)

    def test_mutate(self):
        seed = 0
        random.seed(seed)

        gene = Gene(2)
        gene.mutate(mutation_rate=1)
        self.assertNotEqual(gene.value, 2)

    def test_mutate_alphabet(self):
        seed = 1
        random.seed(seed)

        gene = Gene("A")
        gene.mutate(mutation_rate=1, use_value_pool=True)
        self.assertTrue(gene.value in Config.get_value_pool())

    def test_mutate_alpha_to_number(self):
        gene = Gene("A")
        seed = 0
        while gene.value in Config.get_value_pool() and seed < 100:
            seed += 1
            random.seed(seed)
            gene.mutate(mutation_rate=1, use_value_pool=True)

        self.assertTrue(gene.value not in Config.get_value_pool())

    def test_mutate_number_to_alpha(self):
        seed = 1
        random.seed(seed)
        gene = Gene(2)
        gene.mutate(mutation_rate=1, use_value_pool=True)
        self.assertTrue(gene.value in Config.get_value_pool())

    def test_mutate_alpha_to_number_no_pool(self):
        seed = 1
        random.seed(seed)
        gene = Gene("A")
        gene.mutate(mutation_rate=1, use_value_pool=False)
        self.assertFalse(gene.value in Config.get_value_pool())

    def test_initialize(self):
        gene = Gene()
        gene.initialize(use_value_pool=True)
        self.assertTrue(gene.value is not None)

    def test_initialize2(self):
        gene = Gene(initialize=True)
        self.assertTrue(gene.value is not None)

    def test_copy(self):
        gene = Gene(2)
        copy_gene = gene.copy()
        self.assertEqual(gene.value, copy_gene.value)
        self.assertNotEqual(gene, copy_gene)

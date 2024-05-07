import unittest

from custom_gene import CustomGene
from gene import Gene


class TestGene(unittest.TestCase):
    def test_gene(self):
        gene = Gene("A")
        self.assertEqual(gene.value, "A")
        gene = Gene("B")
        self.assertEqual(gene.value, "B")
        gene = Gene(2)
        self.assertEqual(gene.value, 2)

    def test_custom_gene(self):
        class ArmorGene:
            def __init__(self, name, defense):
                self.name = name
                self.defense = defense
                self.equipped = True
                self.slots = [[1, 2], [3, 4], [5, 6]]

        gene = Gene(ArmorGene("Iron Armor", 10))
        self.assertEqual(gene.value.name, "Iron Armor")
        self.assertEqual(gene.value.defense, 10)
        self.assertEqual(gene.value.equipped, True)
        self.assertEqual(gene.value.slots, [[1, 2], [3, 4], [5, 6]])

    def test_gene_copy(self):
        gene = Gene("A")
        gene_copy = gene.copy()
        self.assertEqual(gene.value, gene_copy.value)
        self.assertNotEqual(gene, gene_copy)
        gene_copy.value = "B"
        self.assertNotEqual(gene.value, gene_copy.value)

    def test_custom_gene_copy(self):
        class ArmorGene:
            def __init__(self, name, defense):
                self.name = name
                self.defense = defense
                self.equipped = True
                self.slots = [[1, 2], [3, 4], [5, 6]]

        gene = Gene(ArmorGene("Iron Armor", 10))
        gene_copy = gene.copy()
        self.assertEqual(gene.value.name, gene_copy.value.name)
        self.assertEqual(gene.value.defense, gene_copy.value.defense)
        self.assertEqual(gene.value.equipped, gene_copy.value.equipped)
        self.assertEqual(gene.value.slots, gene_copy.value.slots)
        self.assertNotEqual(gene, gene_copy)
        gene_copy.value.name = "Steel Armor"
        self.assertNotEqual(gene.value.name, gene_copy.value.name)

    def test_mutate(self):
        value = "A"
        gene = Gene(value)
        self.assertEqual(gene.value, value)
        gene.mutate()
        self.assertEqual(gene.value, value)

    def test_mutation_range(self):
        gene = Gene()
        self.assertEqual(gene.value, None)

        gene.mutate(min_value=0, max_value=10)
        self.assertTrue(0 <= gene.value <= 10)

        gene.mutate(min_value=-5, max_value=-1)
        self.assertTrue(-5 <= gene.value <= -1)

    def test_custom_gene_values(self):
        gene = Gene()
        gene.value_pool = ["A", "B", "C"]
        gene.mutate()
        self.assertIn(gene.value, gene.value_pool)

    def test_custom_gene_mutation(self):
        class ArmorGene(CustomGene):
            def __init__(self, name, defense):
                self.name = name
                self.defense = defense
                self.equipped = True
                self.slots = [[1, 2], [3, 4], [5, 6]]

            def mutate(self):
                self.name = "Steel Armor"
                self.defense = 20
                self.equipped = False
                self.slots = [[2, 3], [4, 5], [6, 7]]

        gene = Gene(ArmorGene("Iron Armor", 10))
        self.assertEqual(gene.value.name, "Iron Armor")
        self.assertEqual(gene.value.defense, 10)
        self.assertEqual(gene.value.equipped, True)
        self.assertEqual(gene.value.slots, [[1, 2], [3, 4], [5, 6]])

        gene.mutate()
        self.assertNotEqual(gene.value.name, "Iron Armor")
        self.assertNotEqual(gene.value.defense, 10)
        self.assertNotEqual(gene.value.equipped, True)
        self.assertNotEqual(gene.value.slots, [[1, 2], [3, 4], [5, 6]])

    def test_custom_gene_mutation2(self):
        class ArmorGene(CustomGene):
            def __init__(self, name, defense):
                self.name = name
                self.defense = defense
                self.equipped = True
                self.slots = [[1, 2], [3, 4], [5, 6]]

            def mutate(self):
                self.name = "Steel Armor"
                self.defense = 20
                self.equipped = False
                self.slots = [[2, 3], [4, 5], [6, 7]]

        gene = ArmorGene("Iron Armor", 10)
        self.assertEqual(gene.name, "Iron Armor")
        self.assertEqual(gene.defense, 10)
        self.assertEqual(gene.equipped, True)
        self.assertEqual(gene.slots, [[1, 2], [3, 4], [5, 6]])

        gene.mutate()
        self.assertNotEqual(gene.name, "Iron Armor")
        self.assertNotEqual(gene.defense, 10)
        self.assertNotEqual(gene.equipped, True)
        self.assertNotEqual(gene.slots, [[1, 2], [3, 4], [5, 6]])


"""
    def test_custom_gene_mutation_value_pool(self):
        class ArmorGene(CustomGene):
            def __init__(self, name, defense):
                self.name = name
                self.defense = defense
                self.equipped = True
                self.slots = [[1, 2], [3, 4], [5, 6]]

            def mutate(self):
                self.name = "Steel Armor"
                self.defense = 20
                self.equipped = False
                self.slots = [[2, 3], [4, 5], [6, 7]]

        gene = Gene()
        gene.value_pool = [Gene(ArmorGene("Iron Armor", 10))]
        gene.mutate()

        self.assertEqual(gene.value.name, "Iron Armor")
        self.assertEqual(gene.value.defense, 10)
        self.assertEqual(gene.value.equipped, True)
        self.assertEqual(gene.value.slots, [[1, 2], [3, 4], [5, 6]])
"""

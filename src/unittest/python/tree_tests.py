import unittest
from corpy.tree import *

class TreeTest(unittest.TestCase):
    def test_one_level_manipulation(self):
        tree = Tree()
        tree["foo"] = "bar"
        self.assertEqual(tree["foo"](), "bar")
        self.assertEqual(tree["foo"].value, "bar")
        tree["foo"].value = "baz"
        self.assertEqual(tree["foo"](), "baz")
        
    def test_one_level_init_state(self):
        tree = Tree()
        self.assertEqual(tree["bar"](), EMPTY_VALUE)
        self.assertEqual(tree["bar"].value, EMPTY_VALUE)
        
    def test_few_levels_manipulation(self):
        tree = Tree()
        tree["foo"][1]["baz"] = "bar"
        self.assertEqual(tree["foo"][1]["baz"](), "bar")
        self.assertEqual(tree["foo"][1]["baz"].value, "bar")
        self.assertEqual(tree["foo", 1, "baz"](), "bar")
        self.assertEqual(tree["foo", 1, "baz"].value, "bar")
        tree["foo", 1, "baz"].value = 3
        self.assertEqual(tree["foo"][1]["baz"](), 3)
        self.assertEqual(tree["foo"][1]["baz"].value, 3)
        self.assertEqual(tree["foo", 1, "baz"](), 3)
        self.assertEqual(tree["foo", 1, "baz"].value, 3) 

    def test_few_levels_init_state(self):
        tree = Tree()
        self.assertEqual(tree["baz"][4]["bar"](), EMPTY_VALUE)
        self.assertEqual(tree["baz"][4]["bar"].value, EMPTY_VALUE)
        self.assertEqual(tree["baz", 4, "bar"](), EMPTY_VALUE)
        self.assertEqual(tree["baz", 4, "bar"].value, EMPTY_VALUE)

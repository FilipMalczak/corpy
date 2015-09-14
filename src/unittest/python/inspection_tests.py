import unittest
import numbers
from corpy.inspection import *

class A:
    def __init__(self):
        self.x = 5
        self.y = 9
        self.foo = "n"

class B:
    __slots__ = ["a", "b"]
    
class C(B):
    def __init__(self):
        self.a = 1
        self.b = 2

class InspectionTests(unittest.TestCase):
    def setUp(self):
        self.a = A()
        self.b = B()
        self.c = C()
    
    def test_dict(self):
        self.assertEqual(
            get_dict(self.a), 
            {
                "x": 5, 
                "y": 9, 
                "foo": "n"
            }
        )
    
    def test_empty_slots(self):
        self.assertEqual(
            get_dict(self.b),
            {
                "a": None,
                "b": None
            }
        )
    
    def test_initialized_slots(self):
        self.assertEqual(
            get_dict(self.c),
            {
                "a": 1,
                "b": 2
            }
        )
    
    def test_class_search(self):
        self.assertEqual(
            search_dict_for_class(self.a, numbers.Number, True),
            {
                "x": 5, 
                "y": 9
            }
        )
        self.assertEqual(
            search_dict_for_class(self.a, numbers.Number, False),
            {}
        )
        self.assertEqual(
            search_dict_for_class(self.a, int, True),
            {
                "x": 5, 
                "y": 9
            }
        )
        self.assertEqual(
            search_dict_for_class(self.a, int, False),
            {
                "x": 5, 
                "y": 9
            }
        )
    
    def test_isoftype(self):
        self.assertTrue(isoftype("abc", str))
        self.assertFalse(isoftype("abc", int))
        self.assertTrue(isoftype("abc", (str, int)))
        self.assertFalse(isoftype("abc", (int, float)))
        self.assertFalse(isoftype("abc", tuple()))

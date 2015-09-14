import unittest

from corpy.descriptors import *

def foo(continuation, obj, objtype):
    val = continuation()
    if val % 2:
        return val
    return val / 2
    
def bar(continuation, obj, objtype):
    return obj._x

class DescriptorTests(unittest.TestCase):
    backed_prop = BackedProperty(1)
    x = HookableDescriptor(at_get = [ foo, bar ])
    y = HookableDescriptor(BackedProperty(1), at_get = [foo])

    def setUp(self):
        self._x = 1
        
    
    def test_backed_prop(self):
        self.assertEqual(self.backed_prop, 1)
        self.backed_prop = 4
        self.assertEqual(self.backed_prop, 4)
    
    def test_hookable_prop(self):
        self.assertEqual(self.x, 1)
        self._x = 6
        self.assertEqual(self.x, 3)
        self.assertEqual(self.y, 1)
        self.y = 6
        self.assertEqual(self.y, 3)

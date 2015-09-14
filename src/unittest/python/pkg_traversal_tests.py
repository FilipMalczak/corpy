import unittest
import test_pkg
import test_pkg.mod1
import test_pkg.sub_pkg
import test_pkg.sub_pkg.mod2
from corpy.package_traversal import visit_package

class TraversalTest(unittest.TestCase):
    def test_traversal(self):
        listed = set([])
        def callback(mod):
            listed.add(mod.__name__)
        visit_package("test_pkg", callback)
        self.assertEqual(listed, set("test_pkg test_pkg.mod1 test_pkg.sub_pkg test_pkg.sub_pkg.mod2".split()))
        #self.assertEqual(listed, set([test_pkg, test_pkg.mod1, test_pkg.sub_pkg, test_pkg.sub_pkg.mod2]))

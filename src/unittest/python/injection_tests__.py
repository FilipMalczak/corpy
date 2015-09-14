import unittest
from corpy.injection import *
from testing_utils import reported

def simple_injection():
    inject("simple_injection_val", 1)

def two_level_injection_nested():
    inject("two_level_injection_val", 1, offset=1)

def two_level_injection():    
    two_level_injection_nested()

def skipped_frame_injection_nested():
    print("skipped_frame_injection_nested", current_skip_offset())
    inject("skipped_frame_injection_val", 1)

def skipped_frame_injection():
    b = 2
    with skip_frame():
        c = 3
        skipped_frame_injection_nested()

def ignore_skip_frame_injection_nested():
    print("ignore_skip_frame_injection_nested", current_skip_offset())
    inject("ignore_skip_frame_injection_val", 1, 1, False)

def ignore_skip_frame_injection():
    with skip_frame():
        ignore_skip_frame_injection_nested()

class TestInjection(unittest.TestCase):
    @reported
    def test_simple_injection(self):
        simple_injection()
        self.assertEqual(simple_injection_val, 1)
    @reported
    def test_two_level_injection(self):
        two_level_injection()
        self.assertEqual(simple_injection_val, 1)
    @reported
    def test_skipped_frame_injection(self):
        a = 1
        skipped_frame_injection()
        self.assertEqual(skipped_frame_injection_val, 1)
    @reported
    def test_ignore_skip_frame_injection(self):
        ignore_skip_frame_injection()
        self.assertEqual(ignore_skip_frame_injection_val, 1)



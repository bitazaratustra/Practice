# pylint: disable-all

import unittest
import sys
from calc import main

class TestCalc(unittest.TestCase):
    def test_4_plus_5(self):
        sys.argv = ["", "4", "+", "5"]
        self.assertEqual(main(), 9)

    def test_2_times_6(self):
        sys.argv = ["", "2", "*", "6"]
        self.assertEqual(main(), 12)

    def test_3_minus_9(self):
        sys.argv = ["", "3", "-", "9"]
        self.assertEqual(main(), -6)

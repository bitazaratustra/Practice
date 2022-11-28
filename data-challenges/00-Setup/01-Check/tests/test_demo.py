# pylint: disable-all

import unittest
from demo import circle_area

class TestDemo(unittest.TestCase):
    def test_returns_3_14_for_radius_1(self):
        expected = 3.14
        actual = circle_area(1)
        self.assertAlmostEqual(expected, actual, 2)

    def test_returns_78_5_for_radius_5(self):
        expected = 78.5
        actual = circle_area(5)
        self.assertAlmostEqual(expected, actual, 1)

    def test_returns_zero_for_negative_radius(self):
        self.assertEqual(circle_area(-1), 0)

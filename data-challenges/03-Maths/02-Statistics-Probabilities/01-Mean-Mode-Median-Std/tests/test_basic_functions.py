# pylint: disable-all

import unittest
import statistics
from basic_functions import my_mean, my_median, my_mode, my_standard_deviation


class TestBasicFunctions(unittest.TestCase):
    def test_my_mean(self):
        test1 = [5, 7, 2, 2, 7, 9, 30, 20, 2, 6, 44, 44, 4, 4, 225]
        self.assertAlmostEqual(my_mean(test1), statistics.mean(test1), places=5)

    def test_my_standard_deviation(self):
        test1 = [5, 7, 2, 2, 7, 9, 30, 20, 2, 6, 44, 44, 4, 4, 225]
        self.assertAlmostEqual(my_standard_deviation(test1), statistics.stdev(test1), places=5)

    def test_my_median(self):
        test1 = [5, 7, 2, 2, 7, 9, 30, 20, 2, 6, 44, 44, 4, 4, 225]
        self.assertAlmostEqual(my_median(test1), statistics.median(test1), places=5)
        test2 = [5, 3, 4, 6, 0, 2, 1]
        self.assertAlmostEqual(my_median(test2), statistics.median(test2), places=5)
        test3 = [5, 3, 4, 6, 0, 2]
        self.assertAlmostEqual(my_median(test3), statistics.median(test3), places=5)

    def test_my_mode(self):
        test1 = [5, 7, 2, 2, 7, 9, 30, 20, 2, 6, 44, 44, 4, 4, 225]
        self.assertAlmostEqual(my_mode(test1), statistics.mode(test1), places=5)
        test2 = ["a", "a", "b", "c"]
        self.assertAlmostEqual(my_mode(test2), statistics.mode(test2), places=5)
        test3 = [5, 3, 4, 6, 0, 2, 2]
        self.assertAlmostEqual(my_mode(test3), statistics.mode(test3), places=5)

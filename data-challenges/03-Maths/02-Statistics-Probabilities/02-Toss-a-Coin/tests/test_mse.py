import unittest
from comparison import mean_squared_error
import random

class TestMSE(unittest.TestCase):

    # Test for mean_squared_error
    def test_mean_squared_error_3(self):
        expected = 0.0028134877011348966
        self.assertAlmostEqual(mean_squared_error(3, 100), expected, places=4)

    def test_mean_squared_error_100(self):
        expected = 6.897205374274377e-05
        self.assertAlmostEqual(mean_squared_error(100, 100), expected, places=4)


    def test_mean_squared_error_1000(self):
        expected = 1.3931286481455582e-05
        self.assertAlmostEqual(mean_squared_error(1000, 100), expected, places=4)

    def test_mean_squared_error_10000(self):
        expected = 5.88e-07
        self.assertAlmostEqual(mean_squared_error(10000, 100), expected, places=4)


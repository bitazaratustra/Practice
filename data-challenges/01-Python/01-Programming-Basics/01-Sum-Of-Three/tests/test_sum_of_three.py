# pylint: disable-all

import unittest
from sum_of_three import sum3

class TestSumOfThree(unittest.TestCase):
    def test_numbers_0_0_0(self):
        self.assertEqual(sum3(0, 0, 0), 0)

    def test_numbers_1_2_3(self):
        self.assertEqual(sum3(1, 2, 3), 6)

    def test_numbers_4_5_6(self):
        self.assertEqual(sum3(4, 5, 6), 15)

    def test_with_negative_numbers(self):
        self.assertEqual(sum3(-1, 1, 0), 0)

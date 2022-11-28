# pylint: disable-all

import unittest
from currencies import convert

class TestStrings(unittest.TestCase):
    def test_convert_usd_to_eur(self):
        amount = (100, "USD")
        result = convert(amount, "EUR")
        self.assertEqual(85, result)

    def test_convert_chf_to_eur(self):
        amount = (200, "CHF")
        result = convert(amount, "EUR")
        self.assertEqual(172, result)

    def test_convert_gbp_to_eur(self):
        amount = (300, "GBP")
        result = convert(amount, "EUR")
        self.assertEqual(339, result)

    def test_convert_eur_to_gbp(self):
        amount = (339, "EUR")
        result = convert(amount, "GBP")
        self.assertEqual(300, result)

    def test_should_handle_a_missing_rate(self):
        amount = (300, "RMB")
        result = convert(amount, "EUR")
        self.assertEqual(None, result)

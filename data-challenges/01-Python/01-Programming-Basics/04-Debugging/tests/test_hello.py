# pylint: disable-all

import unittest
from hello import full_name

class TestHello(unittest.TestCase):
    def test_happy_path(self):
        actual = full_name("george", "harrison")
        self.assertEqual(actual, "George Harrison")

    def test_empty_arguments(self):
        actual = full_name("", "")
        self.assertEqual(actual, "")

    def test_only_first_name(self):
        actual = full_name("ringo", "")
        self.assertEqual(actual, "Ringo")

    def test_only_last_name(self):
        actual = full_name("", "LENNON")
        self.assertEqual(actual, "Lennon")

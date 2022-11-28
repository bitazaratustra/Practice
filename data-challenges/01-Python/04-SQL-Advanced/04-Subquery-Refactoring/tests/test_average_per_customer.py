# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property

from queries import get_average_purchase

class TestAveragePerCustomer(unittest.TestCase):

    @memoized_property
    def stubs(self):
        # Download the database
        subprocess.call(
            [
                "curl", "https://wagon-public-datasets.s3.amazonaws.com/sql_databases/ecommerce.sqlite", "--output",
                "data/ecommerce.sqlite"
            ])

    def setUp(self):
        super().setUp()
        self.stubs
        conn = sqlite3.connect('data/ecommerce.sqlite')
        self.db = conn.cursor()

    def test_type_results(self):
        results = get_average_purchase(self.db)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], tuple)

    def test_length_results(self):
        results = get_average_purchase(self.db)
        self.assertEqual(len(results), 5)

    def test_results(self):
        results = get_average_purchase(self.db)
        expected = [(1, 673.9), (2, 1031.24), (3, 266.32), (4, 2175.03), (5, 1096.3)]
        self.assertEqual(results[0], expected[0])
        self.assertEqual(results[-1], expected[-1])

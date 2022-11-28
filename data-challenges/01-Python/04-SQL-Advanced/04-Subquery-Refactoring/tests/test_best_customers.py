# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property
from queries import best_customers

class TestBestCustomers(unittest.TestCase):

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
        results = best_customers(self.db)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], tuple)

    def test_length_results(self):
        results = best_customers(self.db)
        self.assertEqual(len(results), 3)

    def test_results(self):
        results = best_customers(self.db)
        expected = [(4, 2175.03), (5, 1096.3), (2, 1031.24)]
        self.assertEqual(results, expected)

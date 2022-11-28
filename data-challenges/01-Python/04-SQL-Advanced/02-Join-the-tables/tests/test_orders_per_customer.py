# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property

from queries import orders_per_customer

class TestOrdersPerCustomer(unittest.TestCase):

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

    def test_length_results(self):
        results = orders_per_customer(self.db)
        self.assertEqual(len(results), 6)

    def test_first_result(self):
        results = orders_per_customer(self.db)
        expected = ('Sebastien Saunier', 0)
        self.assertEqual(results[0], expected)

    def test_last_result(self):
        results = orders_per_customer(self.db)
        expected = ('Jim Wood', 6)
        self.assertEqual(results[-1], expected)

    def test_type_result(self):
        results = orders_per_customer(self.db)
        self.assertIsInstance(results, list)

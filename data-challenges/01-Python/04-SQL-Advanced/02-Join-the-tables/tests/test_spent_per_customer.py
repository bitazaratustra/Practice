# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property

from queries import spent_per_customer

class TestSpentCustomer(unittest.TestCase):

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
        results = spent_per_customer(self.db)
        self.assertIsInstance(results, list)

    def test_first_result(self):
        results = spent_per_customer(self.db)
        expected = ('Jim Wood', 1597.9)
        self.assertEqual(results[0], expected)

    def test_last_result(self):
        results = spent_per_customer(self.db)
        expected = ('Toni Faucet', 8700.1)
        self.assertEqual(results[len(results)-1], expected)

    def test_len_resultts(self):
        results = spent_per_customer(self.db)
        self.assertEqual(len(results), 5)

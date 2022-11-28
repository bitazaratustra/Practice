# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property

from queries import detailed_orders

class TestDetailOrders(unittest.TestCase):

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
        results = detailed_orders(self.db)
        self.assertEqual(len(results), 20)

    def test_type_results(self):
        results = detailed_orders(self.db)
        self.assertIsInstance(results, list)

    def test_last_results(self):
        results = detailed_orders(self.db)
        expected = (20, 'Jim Wood', 'James')
        self.assertEqual(results[len(results) - 1], expected)

    def test_first_results(self):
        results = detailed_orders(self.db)
        expected = (1, 'Dick Terrcotta', 'James')
        self.assertEqual(results[0], expected)

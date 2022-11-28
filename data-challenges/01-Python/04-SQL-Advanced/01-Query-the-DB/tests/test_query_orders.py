# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property

from queries import query_orders

class TestQueryOrders(unittest.TestCase):

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

    def test_length_list(self):
        results = query_orders(self.db)
        self.assertEqual(len(results), 20)

    def test_first_element(self):
        results = query_orders(self.db)
        result_0 = results[0]
        expected = (1, 1, 1, '2012-01-04', '2012-01-09', '2012-01-05', 1, 3.75)
        self.assertEqual(result_0, expected)

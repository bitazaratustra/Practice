# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property

from queries import top_ordered_product_per_customer

class TestTopOrderedProductPerCustomer(unittest.TestCase):

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

    expected = [
        (4, 6, 5876),
        (2, 5, 2791.6),
        (1, 6, 1909.7),
        (3, 3, 1200),
        (5, 6, 1175.2)
    ]

    def test_result_type(self):
        results = top_ordered_product_per_customer(self.db)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], tuple)

    def test_result_length(self):
        results = top_ordered_product_per_customer(self.db)
        self.assertEqual(len(results), len(TestTopOrderedProductPerCustomer.expected))

    def test_result_values(self):
        results = top_ordered_product_per_customer(self.db)
        self.assertEqual(results[0], TestTopOrderedProductPerCustomer.expected[0])
        self.assertEqual(results[-1], TestTopOrderedProductPerCustomer.expected[-1])

# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property

from queries import best_employee

class TestBestEmployee(unittest.TestCase):

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
        results = best_employee(self.db)
        self.assertEqual(len(results), 3)

    def test_first_name_in_results(self):
        results = best_employee(self.db)
        self.assertTrue('Patty' in results)

    def test_last_name_in_results(self):
        results = best_employee(self.db)
        self.assertTrue('Lee' in results)

    def test_amount_in_results(self):
        results = best_employee(self.db)
        self.assertTrue(7945.6 in results)

    def test_type_result(self):
        results = best_employee(self.db)
        self.assertIsInstance(results, tuple)

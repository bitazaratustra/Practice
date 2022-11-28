# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property

from queries import get_general_avg_order

class TestGeneralAverage(unittest.TestCase):

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
        results = get_general_avg_order(self.db)
        self.assertIsInstance(results, float)

    def test_results(self):
        results = get_general_avg_order(self.db)
        self.assertGreaterEqual(results, 983)
        self.assertLessEqual(results, 984)

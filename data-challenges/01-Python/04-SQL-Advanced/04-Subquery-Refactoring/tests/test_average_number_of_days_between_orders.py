# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property

from queries import average_number_of_days_between_orders

class TestAverageNumberOfDaysBetweenOrders(unittest.TestCase):

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

    def test_result_type(self):
        result = average_number_of_days_between_orders(self.db)
        self.assertIsInstance(result, int)

    def test_result_value(self):
        result = average_number_of_days_between_orders(self.db)
        expected = 89
        self.assertEqual(result, expected)

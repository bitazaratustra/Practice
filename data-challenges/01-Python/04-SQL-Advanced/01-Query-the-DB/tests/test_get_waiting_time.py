# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property

from queries import get_waiting_time

class TestWaitingTime(unittest.TestCase):

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

    def test_size_list(self):
        results = get_waiting_time(self.db)
        self.assertEqual(len(results), 20)

    def test_type_results(self):
        results = get_waiting_time(self.db)
        self.assertIsInstance(results, list)

    def test_first_result(self):
        results = get_waiting_time(self.db)
        expected = \
            (1, 1, 1, '2012-01-04', '2012-01-09', '2012-01-05', 1, 3.75, 1.0)
        self.assertEqual(results[0], expected)

    def test_last_result(self):
        results = get_waiting_time(self.db)
        expected = \
            (19, 2, 4, '2013-02-21', '2013-02-26', '2013-03-01', 4, 14.0, 8.0)
        self.assertEqual(results[len(results) - 1], expected)

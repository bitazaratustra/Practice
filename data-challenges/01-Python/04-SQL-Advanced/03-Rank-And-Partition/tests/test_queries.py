# pylint: disable-all
import unittest
import sqlite3
import subprocess
from memoized_property import memoized_property

from queries import order_rank_per_customer, order_cumulative_amount_per_customer

class TestQueries(unittest.TestCase):

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

    def test_order_rank_per_customer(self):
        results = order_rank_per_customer(self.db)
        expected = [
            (1, 1, '2012-01-04', 1),
            (8, 1, '2012-06-13', 2),
            (12, 1, '2012-09-13', 3),
            (2, 2, '2012-01-27', 1),
            (4, 2, '2012-03-13', 2),
            (9, 2, '2012-07-06', 3),
            (14, 2, '2012-10-29', 4),
            (19, 2, '2013-02-21', 5),
            (6, 3, '2012-04-28', 1),
            (10, 3, '2012-07-29', 2),
            (11, 3, '2012-08-21', 3),
            (16, 3, '2012-12-14', 4),
            (18, 3, '2013-01-29', 5),
            (20, 3, '2013-03-16', 6),
            (3, 4, '2012-02-19', 1),
            (5, 4, '2012-04-05', 2),
            (7, 4, '2012-05-21', 3),
            (15, 4, '2012-11-21', 4),
            (13, 5, '2012-10-06', 1),
            (17, 5, '2013-01-06', 2)
        ]
        self.assertIs(type(results), list)
        self.assertIs(type(results[0]), tuple)
        self.assertEqual(len(results), len(expected))
        self.assertEqual(results[0], expected[0])
        self.assertEqual(results[-1], expected[-1])

    def test_order_cumulative_amount_per_customer(self):
        results = order_cumulative_amount_per_customer(self.db)
        results = [ (result[0], result[1], result[2], round(result[3], 1)) for result in results ]
        expected = [
            (1, 1, '2012-01-04', 48.0),
            (8, 1, '2012-06-13', 1989.7),
            (12, 1, '2012-09-13', 2021.7),
            (2, 2, '2012-01-27', 1948.7),
            (4, 2, '2012-03-13', 2348.7),
            (9, 2, '2012-07-06', 2648.7),
            (14, 2, '2012-10-29', 3529.7),
            (19, 2, '2013-02-21', 5156.2),
            (6, 3, '2012-04-28', 384.5),
            (10, 3, '2012-07-29', 517.7),
            (11, 3, '2012-08-21', 938.9),
            (16, 3, '2012-12-14', 1146.4),
            (18, 3, '2013-01-29', 1431.9),
            (20, 3, '2013-03-16', 1597.9),
            (3, 4, '2012-02-19', 2395.9),
            (5, 4, '2012-04-05', 6034.5),
            (7, 4, '2012-05-21', 7356.0),
            (15, 4, '2012-11-21', 8700.1),
            (13, 5, '2012-10-06', 250.0),
            (17, 5, '2013-01-06', 2192.6)
        ]
        self.assertIs(type(results), list)
        self.assertIs(type(results[0]), tuple)
        self.assertEqual(len(results), len(expected))
        self.assertEqual(results[0], expected[0])
        self.assertEqual(results[-1], expected[-1])

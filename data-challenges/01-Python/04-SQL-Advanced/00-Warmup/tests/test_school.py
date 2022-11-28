# pylint: disable-all
import unittest
import sqlite3
from memoized_property import memoized_property
import subprocess

from school import students_from_city

class TestSchool(unittest.TestCase):

    @memoized_property
    def stubs(self):
        # Download the database
        subprocess.call(
            [
                "curl", "https://wagon-public-datasets.s3.amazonaws.com/sql_databases/school.sqlite", "--output",
                "data/school.sqlite"
            ])

    def setUp(self):
        super().setUp()
        self.stubs
        conn = sqlite3.connect('data/school.sqlite')
        self.db = conn.cursor()

    def test_paris(self):
        results = students_from_city(self.db, 'Paris')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 5)

    def test_london(self):
        results = students_from_city(self.db, 'London')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 2)

    def test_berlin(self):
        results = students_from_city(self.db, 'Berlin')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 2)

    def test_brussels(self):
        results = students_from_city(self.db, 'Brussels')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 1)

    def test_barcelona(self):
        results = students_from_city(self.db, 'Barcelona')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 0)

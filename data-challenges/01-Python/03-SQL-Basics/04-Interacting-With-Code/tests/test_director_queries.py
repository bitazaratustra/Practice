import unittest
import sqlite3
from yaml import load, FullLoader
from os import path
from memoized_property import memoized_property
import subprocess

from queries import directors_count, directors_list, directors_named_like_count

with open(path.join(path.dirname(__file__), 'results.yml'), encoding='utf-8') as f:
    results = load(f, Loader=FullLoader)

class TestDirectorQueries(unittest.TestCase):
    @memoized_property
    def stubs(self):
        # Download the database
        subprocess.call(
            [
                "curl", "https://wagon-public-datasets.s3.amazonaws.com/sql_databases/movies.sqlite", "--output",
                "data/movies.sqlite"
            ])

    def setUp(self):
        super().setUp()
        self.stubs
        conn = sqlite3.connect('data/movies.sqlite')
        self.db = conn.cursor()

    def test_directors_count_is_integer(self):
        count = directors_count(self.db)
        self.assertIsInstance(count, int)

    def test_directors_count_value(self):
        count = directors_count(self.db)
        self.assertEqual(count, 4089)

    def test_directors_list_is_list(self):
        response = directors_list(self.db)
        self.assertIsInstance(response, list)

    def test_directors_list_size(self):
        directors = results['directors']
        response = directors_list(self.db)
        self.assertEqual(len(response), len(directors))

    def test_directors_list_is_sorted(self):
        response = directors_list(self.db)
        sorted_response = sorted(response)
        self.assertEqual(response, sorted_response)

    def test_directors_list_is_comnplete(self):
        directors = results['directors']
        response = directors_list(self.db)
        self.assertEqual(response, directors)

    def test_directors_named_like_count_is_integer(self):
        directors_count = directors_named_like_count(self.db, "kubric")
        self.assertIsInstance(directors_count, int)

    def test_directors_named_like_count_values(self):
        directors_count = directors_named_like_count(self.db, "kubric")
        self.assertEqual(directors_count, 1)
        directors_count = directors_named_like_count(self.db, "john")
        self.assertEqual(directors_count, 131)

    def test_input_escaping(self):
        malicious_name = "/*malicious code*/you_should_prevent_sql_injection"
        directors_count = directors_named_like_count(self.db, malicious_name)
        self.assertEqual(directors_count, 0)

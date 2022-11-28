# pylint: disable-all

import unittest
from bs4 import BeautifulSoup

class Users(unittest.TestCase):

    def test_users_table_exists(self):
        with open('movies.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
            t.append(table['name'])
        self.assertEqual('users' in t, True)

    def test_users_should_have_the_correct_fields(self):
        with open('movies.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "users"})
        fields = [row.get('name') for row in table[0].find_all('row')]
        correct_fields = ['first_name', 'last_name', 'email', 'age', 'id']
        fields.sort()
        correct_fields.sort()
        self.assertEqual(fields, correct_fields)

    def test_movies_table_exists(self):
        with open('movies.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
            t.append(table['name'])
        self.assertEqual('movies' in t, True)

    def test_movies_should_have_the_correct_fields(self):
        with open('movies.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "movies"})
        fields = [row.get('name') for row in table[0].find_all('row')]
        correct_fields = ['title', 'release_year', 'id', 'rating']
        fields.sort()
        correct_fields.sort()
        self.assertEqual(fields, correct_fields)

    def test_views_table_exists(self):
        with open('movies.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
            t.append(table['name'])
        self.assertEqual('views' in t, True)

    def test_views_should_have_the_correct_fields(self):
        with open('movies.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "views"})
        fields = [row.get('name') for row in table[0].find_all('row')]
        correct_fields = ['date', 'user_id', 'movie_id', 'id']
        fields.sort()
        correct_fields.sort()
        self.assertEqual(fields, correct_fields)

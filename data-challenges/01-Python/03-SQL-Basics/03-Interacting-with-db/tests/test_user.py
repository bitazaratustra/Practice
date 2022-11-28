# pylint: disable-all

import unittest
from bs4 import BeautifulSoup

class Users(unittest.TestCase):

#1 movies
    def test_movies_table_exists(self):
        with open('movies.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
           t.append(table['name'])
        self.assertEqual('movies' in t, True)

#1' correct fields
    def test_movies_should_have_the_correct_fields(self):
        with open('movies.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "movies"})
        t = []
        for row in table[0].find_all('row'):
            t.append(row.get('name'))
            self.assertEqual(row.get('name') in ['title', 'rating', 'vote_count', 'start_year', 'minutes', 'genres', 'director_id', 'imdb_id', 'id'], True)
        self.assertEqual(len(t), 9)

#2 directors
    def test_directors_table_exists(self):
        with open('movies.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
           t.append(table['name'])
        self.assertEqual('directors' in t, True)

#2' correct fields
    def test_directors_should_have_the_correct_fields(self):
        with open('movies.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "directors"})
        t = []
        for row in table[0].find_all('row'):
            t.append(row.get('name'))
            self.assertEqual(row.get('name') in ['name', 'birth_year', 'death_year', 'imdb_director_id', 'id'], True)
        self.assertEqual(len(t), 5)


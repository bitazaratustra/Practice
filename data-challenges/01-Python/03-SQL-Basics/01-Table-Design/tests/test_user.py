# pylint: disable-all

import unittest
from bs4 import BeautifulSoup

class Users(unittest.TestCase):

    def test_users_table_exists(self):
        with open('users.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        self.assertEqual(soup.table['name'],'users')

    def test_should_only_have_users_table(self):
        with open('users.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        self.assertEqual(len(soup.find_all("table")), 1)

    def test_should_have_the_correct_fields(self):
        with open('users.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        fields = [row.get('name') for row in soup.find_all('row')]
        correct_fields = ['id', 'first_name', 'last_name', 'age', 'email']
        fields.sort()
        correct_fields.sort()
        self.assertEqual(fields, correct_fields)

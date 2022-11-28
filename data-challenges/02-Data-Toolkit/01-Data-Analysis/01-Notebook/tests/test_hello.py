# pylint: disable-all

import unittest

from hello import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_says_hello(self):
        self.assertEqual(hello_world(), 'Hello from hello.py')

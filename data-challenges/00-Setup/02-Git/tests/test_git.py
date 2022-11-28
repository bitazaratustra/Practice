# pylint: disable-all

import unittest

from today import *

class TestGit(unittest.TestCase):
    def test_hi_my_name_is(self):
        self.assertGreater(len(my_name_is()), 1)

    def test_my_buddy_is(self):
        self.assertGreater(len(my_buddy_is()), 1)

import unittest
from simulate_reality import play_one_game, play_n_game
import random

class TestReality(unittest.TestCase):
    random.seed(1)
    # Test for play_one_game
    def test_play_one_game_1(self):
        expected = 0
        random.seed(1)
        self.assertEqual(play_one_game(1), expected)

    def test_play_one_game_10(self):
        expected = 5
        random.seed(1)
        self.assertEqual(play_one_game(10), expected)

    def test_play_one_game_100(self):
        expected = 54
        random.seed(1)
        self.assertEqual(play_one_game(100), expected)

    def test_play_one_game_1000(self):
        expected = 515
        random.seed(1)
        self.assertEqual(play_one_game(1000), expected)

    # Test for play_n_game
    def test_play_n_game_1(self):
        expected = 0
        random.seed(1)
        self.assertEqual(play_n_game(1,1)[1], expected)

    def test_play_n_game_100(self):
        expected = 0.24
        random.seed(1)
        self.assertAlmostEqual(play_n_game(100,10)[5], expected, places = 2)

    def test_play_n_game_1000(self):
        expected = 0.08
        random.seed(1)
        self.assertAlmostEqual(play_n_game(1000,100)[50], expected, places = 2)



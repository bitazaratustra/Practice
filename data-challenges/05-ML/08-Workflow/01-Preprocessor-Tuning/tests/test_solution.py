import nbresult
import pandas as pd
import numpy as np
from nbresult import ChallengeResultTestCase


class TestSolution(ChallengeResultTestCase):

    def test_score_good_enough(self):
        self.assertGreater(self.result.cv_score, 0.9)

    def test_n_neighbours(self):
        self.assertEqual(self.result.n_best, 5)

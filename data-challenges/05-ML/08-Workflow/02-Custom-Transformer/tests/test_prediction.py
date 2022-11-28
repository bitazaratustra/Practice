import pandas as pd
import numpy as np
from nbresult import ChallengeResultTestCase


class TestPrediction(ChallengeResultTestCase):

    def test_prediction(self):
        res = self.result.prediction
        if type(res) != float or int:
            res = list(res)[0]
        self.assertGreaterEqual(res, 15)
        self.assertLess(res, 25)

from nbresult import ChallengeResultTestCase
import numpy as np


class TestFeatureAverager(ChallengeResultTestCase):
    def test_solution(self):
        truth_train = np.array([[0.57142857], [0.625], [0.66666667]])

        truth_test = np.array([[0.666667], [0.75], [0.566667]])

        self.assertTrue(np.allclose(self.result.X_train_transformed, truth_train))
        self.assertTrue(np.allclose(self.result.X_test_transformed, truth_test))

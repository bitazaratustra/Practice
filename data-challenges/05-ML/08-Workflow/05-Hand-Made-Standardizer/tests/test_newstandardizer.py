from nbresult import ChallengeResultTestCase
import numpy as np


class TestNewStandardizer(ChallengeResultTestCase):
    def test_solution(self):
        truth_train = np.array([
            [-0.612372, -0.612372, -0.612372],
            [0.000000, 0.000000, 0.000000],
            [0.612372, 0.612372, 0.612372]
        ])
        truth_test = np.array([
            [-0.612372, -1.837117, -3.061862],
            [ 0.        , -1.224745, -2.449490],
            [ 0.612372, -0.612372,  1.224745]])
        self.assertTrue(np.allclose(self.result.X_train_transformed, truth_train))
        self.assertTrue(np.allclose(self.result.X_test_transformed, truth_test))
        
        
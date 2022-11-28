from nbresult import ChallengeResultTestCase
import numpy as np


class TestStandardizer(ChallengeResultTestCase):
    def test_solution(self):
        truth_train = np.array([[-1.22474487, -1.22474487, -1.22474487],
                                [0., 0., 0.],
                                [ 1.22474487,  1.22474487,  1.22474487]])
        truth_test = np.array([[-1.22474487, -3.67423461, -6.12372436],
                               [ 0.        , -2.44948974, -4.89897949],
                               [ 1.22474487, -1.22474487,  2.44948974]])
        self.assertTrue(np.allclose(self.result.X_train_transformed, truth_train))
        self.assertTrue(np.allclose(self.result.X_test_transformed, truth_test))
        
        
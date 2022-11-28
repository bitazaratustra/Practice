from nbresult import ChallengeResultTestCase
import numpy as np


class TestFeatureUnionCustomTransformers(ChallengeResultTestCase):
    def test_solution(self):
        truth_train = np.array([[-0.408248, -0.408248, -0.408248,0.571429],
                                [0., 0., 0., 0.625],
                                [ 0.408248,  0.408248,  0.408248, 0.666667]])
        truth_test = np.array([[-0.408248, -1.224745, -2.041241, 0.666667],
                               [ 0.        , -0.816497, -1.632993, 0.75],
                               [ 0.408248, -0.408248,  0.816497, 0.566667]])

        self.assertTrue(np.allclose(self.result.X_train_transformed, truth_train))
        self.assertTrue(np.allclose(self.result.X_test_transformed, truth_test))

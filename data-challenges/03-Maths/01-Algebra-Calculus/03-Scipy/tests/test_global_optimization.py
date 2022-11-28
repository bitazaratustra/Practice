from nbresult import ChallengeResultTestCase
import numpy as np


class TestGlobalOptimization(ChallengeResultTestCase):
    def test_bounds_values(self):
        for bound in self.result.bounds:
            self.assertEqual(
                bound,
                (-150, 150),
                'Boundaries should be between -150 and 150'
            )

    def test_minimum_shgo_shape(self):
        self.assertEqual(self.result.Xmin_shgo.shape, (2,))

    def test_minimum_dual_shape(self):
        self.assertEqual(self.result.Xmin_dual.shape, (2,))

    def test_minimum_shgo_values(self):
        Xmin = self.result.Xmin_shgo
        self.assertTrue(
            np.all(Xmin <= 150),
            'Make sure the upper boundary is 150'
        )
        self.assertTrue(
            np.all(Xmin >= -150),
            'Make sure the lower boundary is -150'
        )

    def test_minimum_dual_values(self):
        Xmin = self.result.Xmin_dual
        self.assertTrue(
            np.all(Xmin <= 150),
            'Make sure the upper boundary is 150'
        )
        self.assertTrue(
            np.all(Xmin >= -150),
            'Make sure the lower boundary is -150'
        )

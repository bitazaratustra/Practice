from nbresult import ChallengeResultTestCase
import numpy as np


class TestTwoMeans(ChallengeResultTestCase):
    def test_two_clusters(self):
        self.assertEqual(len(np.unique(self.result.clusters)), 2)

    def test_imbalanced_clusters(self):
        _, counts = np.unique(self.result.clusters, return_counts=True)
        self.assertEqual(max(counts) / min(counts), 3)

from nbresult import ChallengeResultTestCase


class TestMissing_values(ChallengeResultTestCase):
    def test_nans(self):
        self.assertEqual(self.result.dataset.isnull().sum().sum(), 0)

    def test_number_of_columns(self):
        self.assertEqual(len(self.result.dataset.columns), 9)

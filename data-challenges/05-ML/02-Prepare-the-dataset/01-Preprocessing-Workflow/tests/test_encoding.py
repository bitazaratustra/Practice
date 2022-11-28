from nbresult import ChallengeResultTestCase


class TestEncoding(ChallengeResultTestCase):
    def test_columns(self):
        self.assertEqual(len(self.result.dataset.columns), 13)

    def test_central_air(self):
        self.assertEqual(self.result.dataset.CentralAir.max(), 1)

    def test_month_sold_features_number(self):
        self.assertEqual(len(self.result.new_features), 2)

    def test_month_sold_features(self):
        data = self.result.dataset
        for feature in self.result.new_features:
            self.assertEqual(data[feature].max(), 1)

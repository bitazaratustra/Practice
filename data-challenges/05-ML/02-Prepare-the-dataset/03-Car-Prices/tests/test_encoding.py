from nbresult import ChallengeResultTestCase

class TestEncoding(ChallengeResultTestCase):
    def test_aspiration(self):
        self.assertEqual(self.result.dataset.aspiration.max(), 1)
    def test_enginelocation(self):
        self.assertEqual(self.result.dataset.enginelocation.max(), 1)
    def test_enginetype(self):
        self.assertEqual(len(self.result.dataset.columns) > 13, True)
#     def test_cylindernumber(self):
#         self.assertEqual(self.result.dataset.cylindernumber.max(), 1)
    def test_price(self):
        self.assertEqual(self.result.dataset.price.max(), 1)

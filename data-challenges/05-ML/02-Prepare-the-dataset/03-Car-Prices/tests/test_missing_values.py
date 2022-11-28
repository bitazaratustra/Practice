from nbresult import ChallengeResultTestCase

class TestMissing_values(ChallengeResultTestCase):
    def test_engine_location(self):
        self.assertEqual(self.result.dataset.enginelocation.isnull().sum(), 0)
    def test_carwidth(self):
        self.assertEqual(self.result.dataset.carwidth.isnull().sum(), 0)


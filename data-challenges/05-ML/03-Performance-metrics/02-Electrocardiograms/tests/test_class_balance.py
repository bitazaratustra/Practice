from nbresult import ChallengeResultTestCase


class TestClass_balance(ChallengeResultTestCase):
    def test_at_risk_count(self):
        self.assertEqual(self.result.at_risk, 1448)

    def test_healthy_count(self):
        self.assertEqual(self.result.healthy, 18117)

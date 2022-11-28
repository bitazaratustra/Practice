from nbresult import ChallengeResultTestCase

class TestWaitTime(ChallengeResultTestCase):

    def test_wait_time(self):
        self.assertEqual(self.result.shape, (96478, 5))

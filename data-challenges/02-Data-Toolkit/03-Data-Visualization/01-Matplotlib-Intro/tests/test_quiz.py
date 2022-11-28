from nbresult import ChallengeResultTestCase


class TestQuiz(ChallengeResultTestCase):
    def test_continuous_function_representation(self):
        self.assertEqual(self.result.answer1, 'plot()')

    def test_relationship_representation(self):
        self.assertEqual(self.result.answer2, 'scatter()')

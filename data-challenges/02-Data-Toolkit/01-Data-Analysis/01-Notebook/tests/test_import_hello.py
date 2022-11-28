from nbresult import ChallengeResultTestCase

class TestImportHello(ChallengeResultTestCase):
    def test_method_returns_a_string(self):
        self.assertEqual(type(self.result.sentence), str)

    def test_method_returns_correct_sentence(self):
        self.assertEqual(self.result.sentence, "Hello from hello.py")

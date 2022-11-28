from nbresult import ChallengeResultTestCase

class TestX_pad_shape(ChallengeResultTestCase):
    
     def test_variable_X_pad_shape(self):
        self.assertEqual(self.result.X_pad_shape,(87554,187))
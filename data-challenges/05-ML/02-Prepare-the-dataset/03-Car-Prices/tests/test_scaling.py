from nbresult import ChallengeResultTestCase

class TestScaling(ChallengeResultTestCase):
    def test_peakrpm(self):
        self.assertEqual(self.result.dataset.peakrpm.median(), 0)
    def test_carwidth(self):
        self.assertEqual(self.result.dataset.carwidth.median() , 0)
    def test_stroke(self):
        self.assertEqual(self.result.dataset.stroke.median() , 0)
    def test_curbweight(self):
        self.assertEqual(self.result.dataset.curbweight.max() < 3, True)

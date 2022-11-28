from nbresult import ChallengeResultTestCase


class TestScaling(ChallengeResultTestCase):
    def test_roof_surface(self):
        self.assertEqual(self.result.dataset.RoofSurface.max(), 1)

    def test_gr_liv_area(self):
        self.assertEqual(self.result.dataset.GrLivArea.median(), 0)

    def test_bedroom_kitchen_condition(self):
        self.assertEqual(
            self.result.dataset[[
                'BedroomAbvGr',
                'KitchenAbvGr',
                'OverallCond']].min().sum(), 0)
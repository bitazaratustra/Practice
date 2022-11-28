from nbresult import ChallengeResultTestCase
import numpy as np

class TestWarmup(ChallengeResultTestCase):
    def test_dataframe_has_new_columns(self):
        assert np.array_equal(self.result.df_columns, ['url', 'title', 'description'])

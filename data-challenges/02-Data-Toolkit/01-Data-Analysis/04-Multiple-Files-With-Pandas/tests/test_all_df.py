from nbresult import ChallengeResultTestCase


class TestAllDf(ChallengeResultTestCase):
    def test_all_df_shape(self):
        self.assertEqual(self.result.all_df_shape, (30568, 13))

    def test_all_df_columns(self):
        cols = {
            'Athlete', 'City', 'Code', 'Country', 'Discipline', 'Event',
            'GDP per Capita', 'Gender', 'Medal', 'Population', 'Season',
            'Sport', 'Year'
        }
        self.assertEqual(self.result.all_df_columns, cols)

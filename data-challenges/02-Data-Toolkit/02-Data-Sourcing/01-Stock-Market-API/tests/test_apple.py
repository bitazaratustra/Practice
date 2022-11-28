from nbresult import ChallengeResultTestCase


class TestApple(ChallengeResultTestCase):

    def test_apple_df_index_name_is_date(self):
        self.assertEqual(self.result.index_name, 'date')

    def test_apple_df_index_is_timestamp(self):
        self.assertEqual(self.result.index_type, '<M8[ns]', "Check you converted the 'date' colummn into a `datetime`.")

    def test_apple_df_columns(self):
        columns = {
            'close', 'high', 'low', 'open', 'symbol', 'volume', 'id',
            'key', 'subkey', 'updated', 'changeOverTime',
            'marketChangeOverTime', 'uOpen', 'uClose', 'uHigh', 'uLow',
            'uVolume', 'fOpen', 'fClose', 'fHigh', 'fLow', 'fVolume',
            'label', 'change', 'changePercent'
            }
        self.assertEqual(columns.issubset(set(self.result.columns)), True)

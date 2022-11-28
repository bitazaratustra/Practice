from nbresult import ChallengeResultTestCase


class TestReceipts(ChallengeResultTestCase):

    def test_receipts_list(self):
        self.assertEqual(len(self.result.raw), 100)

    def test_receipts_dict(self):
        self.assertEqual(len(self.result.receipts), 3)
        self.assertEqual(len(self.result.receipts['date']), 100)

    def test_receipts_df_size(self):
        self.assertEqual(self.result.df_size, (100, 3))

    def test_receipt(self):
        self.assertEqual(self.result.receipt.date, '15-12-2017')
        self.assertEqual(self.result.receipt.quantity, '148')
        self.assertEqual(self.result.receipt.amount, '1850.00')

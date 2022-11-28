from nbresult import ChallengeResultTestCase


class TestBooks(ChallengeResultTestCase):

    def test_books_df_columns_name(self):
        self.assertEqual(
            list(self.result.columns),
            ['Title', 'Price', 'Rating']
        )

    def test_books_df_columns_size(self):
        self.assertEqual(len(list(self.result.columns)), 3)

    def test_first_book_title(self):
        self.assertTrue('A Light in the' in self.result.title)

    def test_first_book_price(self):
        self.assertEqual(self.result.price, 51.77)

    def test_first_book_rating(self):
        self.assertEqual(self.result.rating, 3)

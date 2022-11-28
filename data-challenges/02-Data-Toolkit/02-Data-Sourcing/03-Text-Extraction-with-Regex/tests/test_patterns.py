import re
from nbresult import ChallengeResultTestCase


class TestPatterns(ChallengeResultTestCase):

    TEXT_TO_SEARCH = """
Receipt Number 107482 ||| 12-12-2017
------------------------------------

Quantity                         193
Total Amount               2605.50 €

====================================
************************************


Receipt Number 107538 ||| 15-12-2017
------------------------------------

Quantity                         148
Total Amount               1850.00 €
        """

    def test_zip_code_pattern(self):
        zip_code_pattern = self.result.zipcode_re
        text_to_search = """13000 is the zip code of Marseille,
            Le Wagon Bdx is located in Bordeaux 33000, France
            city:Lyon,  zip: 69000"""
        zipcodes = re.findall(zip_code_pattern, text_to_search)
        self.assertEqual(zipcodes, ['13000', '33000', '69000'])

    def test_date_pattern(self):
        date_pattern = self.result.date_re
        text_to_search = """
            She was born on the 07-04-1983
            05-05-1986: message sent
            Date: 26-05-2021, Location: Australia, Event: Total lunar eclipse
        """
        dates = re.findall(date_pattern, text_to_search)
        self.assertEqual(dates, ['07-04-1983', '05-05-1986', '26-05-2021'])

    def test_quantity_pattern(self):
        quantity_pattern = self.result.quantity_re
        quantities = re.findall(quantity_pattern, self.TEXT_TO_SEARCH)
        self.assertEqual(quantities, [
            "Quantity                         193",
            "Quantity                         148"
        ])

    def test_amount_pattern(self):
        amount_pattern = self.result.amount_re
        amounts = re.findall(amount_pattern, self.TEXT_TO_SEARCH)
        self.assertEqual(amounts, [
            "Total Amount               2605.50 €",
            "Total Amount               1850.00 €"
        ])

    def test_quantity_group_pattern(self):
        quantity_group_pattern = self.result.quantity_grp_re
        quantities = re.findall(quantity_group_pattern, self.TEXT_TO_SEARCH)
        self.assertEqual(quantities, ['193', '148'])

    def test_amount_group_pattern(self):
        amount_group_pattern = self.result.amount_grp_re
        amounts = re.findall(amount_group_pattern, self.TEXT_TO_SEARCH)
        self.assertEqual(amounts, ['2605.50', '1850.00'])

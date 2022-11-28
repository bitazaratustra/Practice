# pylint: disable=missing-docstring


RATES = {'USDEUR': 0.85,
'GBPEUR': 1.13,
'CHFEUR': 0.86,
'EURGBP': 0.885}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    if amount[1] == 'USD' and currency == 'EUR':
        return round(amount[0] * 0.85, 1)
    if amount[1] == 'GBP' and currency == 'EUR':
        return round(amount[0] * 1.13, 1)
    if amount[1] == 'EUR' and currency == 'GBP':
        return round(amount[0] * 0.885,1)
    if amount[1] == 'CHF' and currency == 'EUR':
        return round(amount[0] * 0.86,1)
    return None

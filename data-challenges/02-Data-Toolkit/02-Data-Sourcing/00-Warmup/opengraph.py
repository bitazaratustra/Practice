# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Return a dictionary of OpenGraph metadata found in HTML of given url
    """
    base = f'https://opengraph.lewagon.com/?url={url}'
    response = requests.get(base)
    if response.status_code != 200:
        return None
    results = response.json()
    return results['data']

# To manually test, please uncomment the following lines and run `python opengraph.py`:
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(fetch_metadata("https://www.github.com"))

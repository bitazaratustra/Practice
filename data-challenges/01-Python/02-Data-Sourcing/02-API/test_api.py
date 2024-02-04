"""Module for handling weather information.

This module provides functions to display the weather forecast for a given city.
"""
import requests

URL = "https://weather.lewagon.com/geo/1.0/direct?q=BuenosAires"
response = requests.get(URL).json()
city = response[0]
print(f"{city['name']}: ({city['lat']}, {city['lon']})")

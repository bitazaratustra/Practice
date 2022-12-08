import requests

url = "https://weather.lewagon.com/geo/1.0/direct?q=Barcelona"
response = requests.get(url).json()
city = response[0]
print(f"{city['name']}: ({city['lat']}, {city['lon']})")

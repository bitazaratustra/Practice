
import sys
import requests

base_uri = "https://weather.lewagon.com"


def search_city(query):
    '''Look for a given city. If multiple options are returned, have the user choose between them.
       Return one city (or None)
    '''
    cities = requests.get(f'{base_uri}/geo/1.0/direct?q={query}&limit=5').json()
    if not cities:
        print(f"Sorry, OpenWeather does not know about {query}...")
        return None
    if len(cities) == 1:
        return cities[0]
    for i, city in enumerate(cities):
        print(f"{i + 1}. {city['name']},{city['country']}")
    index = int(input("Multiple matches found, which city did you mean?\n> ")) - 1
    return cities[index]

def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    params={'lat': lat, 'lon': lon, 'units': 'metric'}
    url = f"{base_uri}/data/2.5/forecast"
    forecasts = requests.get(url, params).json()['list']
    return forecasts[::8]

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    # TODO: Display weather forecast for a given city
    # $CHALLENGIFY_BEGIN
    if city:
        daily_forecasts = weather_forecast(city['lat'], city['lon'])
        for forecast in daily_forecasts:
            max_temp = round(forecast['main']['temp_max'])
            print(f"{forecast['dt_txt'][:10]}: {forecast['weather'][0]['main']} ({max_temp}°C)")


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)






#weather_1 = response['list'][0]['weather'][0]['main']
    #tmp_1 = round(float(response['list'][0]['main']['temp']) - 273.15, 1)
    #weather_2 = response['list'][8]['weather'][0]['main']
    #tmp_2 = round(float(response['list'][8]['main']['temp']) - 273.15, 1)
    #weather_3 = response['list'][16]['weather'][0]['main']
    #tmp_3 = round(float(response['list'][16]['main']['temp']) - 273.15, 1)
    #weather_4 = response['list'][24]['weather'][0]['main']
    #tmp_4 = round(float(response['list'][24]['main']['temp']) - 273.15, 1)
    #weather_5 = response['list'][32]['weather'][0]['main']
    #tmp_5 = round(float(response['list'][32]['main']['temp']) - 273.15, 1)
    #day_1 = response['list'][0]['dt_txt'][0:10]
    #day_2 = response['list'][8]['dt_txt'][0:10]
    #day_3 = response['list'][16]['dt_txt'][0:10]
    #day_4 = response['list'][24]['dt_txt'][0:10]
    #day_5 = response['list'][32]['dt_txt'][0:10]
    #city = response['city']['name']
    #print(f'Here is the weather in {city}')
    #print(f'{day_1}: {weather_1} {tmp_1}')
    #print(f'{day_2}: {weather_2} {tmp_2}')
    #print(f'{day_3}: {weather_3} {tmp_3}')
    #print(f'{day_4}: {weather_4} {tmp_4}')
    #print(f'{day_5}: {weather_5} {tmp_5}')

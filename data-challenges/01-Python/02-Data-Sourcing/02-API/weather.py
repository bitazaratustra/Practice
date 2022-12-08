
import sys
import requests

base_uri = "https://weather.lewagon.com"


def search_city(query):
    '''Look for a given city. If multiple options are returned, have the user choose between them.
       Return one city (or None)
    '''
    response = requests.get(f'{base_uri}/geo/1.0/direct?q={query}').json()
    if len(response) == 0:
        print('This city doesnt exist')
        return main()
    place = response[0]
    return place['lat'], place['lon']

def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    response = requests.get(f'{base_uri}/data/2.5/forecast?lat={lat}&lon={lon}').json()
    for i in range(len(response['list']), len(response['list'][-1]), 7):
        print(response['list'][i]['main']['temp'])

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    try:
        city = search_city(query)
        weather_forecast(city[0], city[1])
    except len(city) == 0:
        TypeError ('Escribiste con los codos!')

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

import requests
import json
from Geocode_parse import GetCoords


def get_base_weather_request(address):
    coords = '41.2439122,-95.9614398'            # switch to GetCoords(address) from static once code block works
    base_url = f'https://api.weather.gov/points/{coords}'
    response = requests.get(base_url)
    if response.status_code == 200:
        base_data = response.json()
        pretty_data = json.dumps(base_data, indent=4)
        print(pretty_data)
        return base_data
    else:
        print(f'Error: Failed to retrieve data {response.status_code}')


def get_weather_forecast(address):
    base_data = get_base_weather_request(address)
    forecast_url = f'{base_data["properties"]["forecast"]}'
    response = requests.get(forecast_url)
    print(json.dumps(response.json(), indent=4))
    print(forecast_url)


test_address = ' '
get_weather_forecast(test_address)
# for alerts and forecast use coords, for forecast discussion need Grid id from properties.


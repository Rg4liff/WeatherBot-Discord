import requests
import json
from Geocode_parse import GetCoords


def validate_address(addre):
    #TODO: validate address MUST HAVE:
    # -state initial and capitalized
    # -Numbers before street name
    # -Have different street suffix that matches list
    # -Be in (street name, city, state initial) form
    # -Add commas if needed
    # return updated corrected address or return None to signal invalid address

    pass


def get_base_weather_request(address):
    #coords = GetCoords(address)            # switch to GetCoords(address) from static once code block works
    coords = '41.2439122,-95.9614398'
    base_url = f'https://api.weather.gov/points/{coords}'
    response = requests.get(base_url)
    if response.status_code == 200:
        base_data = response.json()
        return base_data
    else:
        print(f'Error: Failed to retrieve data {response.status_code}')


def get_weather_forecast(address):
    base_data = get_base_weather_request(address)
    forecast_url = f'{base_data["properties"]["forecast"]}'
    response = requests.get(forecast_url)
    data = json.loads(response.text)
    periods = data['properties']['periods']
    forecast_info = ''

    for period in periods:
        day = period['name']
        forecast = period['detailedForecast']
        forecast_info += f'{day}:\n{forecast}\n\n'

    return forecast_info


if __name__ == '__main__':
    test_address = ' '
    get_weather_forecast(test_address)


# for forecast use coords,
# for forecast discussion need Grid id from properties.
# for alerts use  https://api.weather.gov/alerts/active/zone/{zoneID}

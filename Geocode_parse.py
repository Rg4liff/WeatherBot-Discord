import requests
import os
import json
from dotenv import load_dotenv


load_dotenv()
geocode_token = os.getenv('GEOCODE_TOKEN')
Geocode_base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'


def GetGeocode(address):
    url = f'{Geocode_base_url}address={address}&key={geocode_token}'
    response = requests.get(url)

    if response.status_code == 200:
        geocode_data = response.json()
        return geocode_data
    else:
        print(f'Error: Failed to retrieve data {response.status_code}')


def GetCoords(addr):
    address = addr.replace(' ', '+')
    print(address)
    info = GetGeocode(address)
    print(json.dumps(info, indent=4))
    if info:
        coords = f'{info["results"][0]["geometry"]["location"]["lat"]},{info["results"][0]["geometry"]["location"]["lng"]}'
        return coords


# check if this works first and retrieves prop coords before implementing
if __name__ == '__main__':
    test_address = '1609 S 33rd St, Omaha, NE'
    test_coords = GetCoords(test_address)
    print(test_coords)

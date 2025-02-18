import json


COORD_THRESHOLD = .0225

# TODO:
#  -Build out cache_manager to create and call functions to check or update cache as needed.
#  -Build out timestamp and forecast part of cache

def check_cache_for_address(cache, address):
    for grid_block in cache.values():
        for (lat, lon), stored_address in grid_block['coords'].items():
            if stored_address == address:
                return True, (lat, lon)  # Found the address, return coordinates
    return False, None  # Not found


def check_cache_for_coords(cache, lat, lon, COORD_THRESHOLD):
    for grid_block_id, grid_block in cache.items():
        for existing_lat, existing_lon in grid_block['coords']:
            if abs(lat - existing_lat) <= COORD_THRESHOLD and abs(lon - existing_lon) <= COORD_THRESHOLD:
                return True, grid_block_id  # Found a nearby match
    return False, None  # Not found


def is_nearby(lat1, lon1, lat2, lon2, threshold=COORD_THRESHOLD):
    return abs(lat1 - lat2) <= threshold and abs(lon1 - lon2) <= threshold


def cache_info(cache, response_json, addr):

    grid_block_id = response_json['properties']['gridX'] + ',' + response_json['properties']['gridY']
    grid_station = response_json['properties']['radarStation']
    lat = response_json['geometry']['coordinates'][1]
    lon = response_json['geometry']['coordinates'][0]
    address = addr

    grid_block = cache.setdefault(grid_block_id), {
        'coords': {},
        'grid_stn': {}
    }

    if (lat, lon) not in grid_block['address_coords']:
        grid_block['coords'][(lat, lon)] = address

    #TODO
    # Add timestamp and forecast data check if timestamp is over 24hours old, if so delete and resend request on check
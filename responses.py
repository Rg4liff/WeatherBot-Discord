from random import choice, randint
import Weather_requests
import re

# TODO:
#  Clean up  responses for better readability
#  implement Forecast discussion calls
#  implement Alert calls


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return f'{print_output_options()}'
    elif 'hello' in lowered:
        return f'Hello there! I am your friendly weather chat bot!\n{print_output_options()}'
    elif '!get forecast' in lowered:
        address = lowered[13:].strip()
        output = Weather_requests.get_weather_forecast(address)
        return f'Sure! Here is the 7 day forecast for {address}:\n\n{output}'
    elif '!get alerts:' in lowered:
        address = lowered.split('!get alerts:')
        return"Sorry, that feature isn't ready yet."
    elif '!get forecast discussion' in lowered:
        return "Sorry, that feature isn't ready yet."
    elif '?get forecast' in lowered:
        address = lowered[13:].strip()
        output = Weather_requests.get_weather_forecast(address)
        return f'Sure here is your & day forcast to private chat:\n\n{output}'
    elif '?get alerts:' in lowered:
        "Sorry, that feature isn't ready yet."
    elif '?get forecast discussion' in lowered:
        return "Sorry, that feature isn't ready yet."


def print_output_options():
    option_menu = """Here is a list of input options:
    -!Get Forecast [Address,city,St]- This will give you a 7 day forecast for your area
    -!Get Alerts- This will give you a list of current weather alerts for your area
    -!Get Forecast Discussion- This will give you an in depth meteorological discussion from your local weather office
    
    -?Get Forecast- This will privately send you a 7 day forecast for your area
    -?Get Alerts- This will privately send you a list of current weather alerts for your area
    -?Get Forecast Discussion- This will privately send you an in depth meteorological discussion from your local weather office
    """
    return option_menu

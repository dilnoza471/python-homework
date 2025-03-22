import requests

api_key = 'c2885148415db286d874c45962de98bd'


def get_weather_info(city: str = 'Tashkent') -> None:
    """
    gets weather info from Weather API
    :param city: city name defaults to 'Tashkent'
    :return: None
    prints the info
    """
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(url=base_url, params=params)
    if response.status_code == 200:
        data = response.json()  # Convert JSON response to dictionary
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Error: ", response.status_code)


if __name__ == '__main__':
    get_weather_info('London')

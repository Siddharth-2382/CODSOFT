import os
import dotenv
import requests

# Load the .env file
dotenv.load_dotenv()

API_key = os.environ['API_KEY']
OWM_endpoint = os.environ['OWM_ENDPOINT']


def get_weather_data(city):
    weather_params = {
        "q": city.capitalize(),
        "units": "metric",
        "appid": API_key,
    }
    response = requests.get(url=OWM_endpoint, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()

    data = {
        "weather_description": weather_data['weather'][0]['description'],
        "temperature": weather_data['main']['temp'],
        "humidity": weather_data['main']['humidity'],
        "wind_speed": weather_data['wind']['speed'],
    }

    return data

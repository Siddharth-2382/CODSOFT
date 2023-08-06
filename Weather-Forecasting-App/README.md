# Weather-Forecasting-App

The Weather-Forecasting-App is a simple weather forecasting application built using Tkinter, a Python GUI library, and the OpenWeatherMap API. This app allows users to get weather forecasts for different locations and stay updated on current weather conditions.

## Features

1. **Current Weather**: The app displays the current weather conditions, including temperature, humidity, wind speed, and weather description, for the input location.


2. **Location Search**: The app allows users to search for weather information for different cities or locations.


3. **User-Friendly Interface**: The application has a clean and intuitive user interface, making it easy for users to check the weather forecast.

## Installation and Setup

1. Clone the repository or download the source code as a zip file.

       git clone https://github.com/Siddharth-2382/CODSOFT.git
       cd CODSOFT
       cd Weather-Forecasting-App
2. Ensure you have Python 3.x installed on your system.

3. Install the required dependencies by running the following command in your terminal or command prompt:

       pip install requests

4. Run the `weather_forecasting.py` script using Python:

       python weather_forecasting.py


## How to Use

1. Upon launching the application, the user is presented with a input field to enter the location for which they want to get weather information.


2. Enter the name of the city or location and click the "Get Weather" button.


3. The app will fetch weather data from the OpenWeatherMap API using the `main.py` module and display the current weather conditions and forecast on the GUI.


## Project Structure

- `main.py`: This file handles data fetching and response handling from the OpenWeatherMap API.

- `weather_forecasting.py`: This is the main file that runs the GUI and displays the weather information fetched from `main.py`.

## Technologies Used

- Python
- Tkinter (Python GUI library)
- OpenWeatherMap API

## Acknowledgments

I would like to acknowledge the following:

- CodSoft for providing me with the opportunity to work on this project as part of my internship.
- CodSoft's team for their valuable guidance and support during the development process.

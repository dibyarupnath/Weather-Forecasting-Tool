import requests
import json

def get_weather_forecast(city):
    access_key = 'ec5c2f0b9911f072a9d685dff29cd2a0' # Weatherstack API
    url = f'http://api.weatherstack.com/current?access_key={access_key}&query={city}'
    
    # Weatherstack API
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        
        if response.status_code == 200:
            # Parsing weather data
            location = data['location']['name']
            country = data['location']['country']
            temperature = data['current']['temperature']
            description = data['current']['weather_descriptions'][0]
            humidity = data['current']['humidity']
            wind_speed = data['current']['wind_speed']
            
            # Displaying weather information
            print(f'Current weather in {location}, {country}:')
            print(f'Condition: {description}')
            print(f'Temperature: {temperature}°C')
            print(f'Humidity: {humidity}%')
            print(f'Wind Speed: {wind_speed} km/h')
        else:
            print(f'Error: {data["error"]["info"]}')
            
    except requests.exceptions.RequestException as error:
        print(f'Error: {error}')

# Prompting the user for a city name
city_name = input('Enter a city name: ')
get_weather_forecast(city_name)

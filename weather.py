import requests
import json

def get_weather_forecast(city):
    
    api_key = '2b2b14c04f01b8756f5911d5c61119d9' # OpenWeather API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    # OpenWeather API
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        
        if response.status_code == 200:
            # Parsing weather data
            main_info = data['weather'][0]['main']
            description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            # Displaying weather information
            print(f'Current weather in {city}:')
            print(f'Condition: {main_info} ({description})')
            print(f'Temperature: {temperature}°C')
            print(f'Humidity: {humidity}%')
            print(f'Wind Speed: {wind_speed} m/s')
        else:
            print(f'Error: {data["message"]}')
        
    except requests.exceptions.RequestException as error:
        print(f'Error: {error}')

# Prompting the user for a city name
city_name = input('Enter a city name: ')
get_weather_forecast(city_name)

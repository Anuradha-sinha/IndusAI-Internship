import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_weather(data):
    if data:
        city = data['name']
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {weather}")
        print(f"Humidity: {humidity}%")
        # print(data)
    else:
        print("Error fetching weather data")

if __name__ == "__main__":
    api_key = "c586fd46fabe1f4eac556976d88c76c6" 
    city = input("Enter the city name: ")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

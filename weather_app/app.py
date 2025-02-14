import requests

api_key = 'f343ca3a5ec4f731a75ec2583844b49b'


user_input = input("Enter city:")


weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No city Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is:, {weather}")
    print(f"The temperature in {user_input} is:, {temp}*D")


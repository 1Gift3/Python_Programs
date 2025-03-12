import requests

city_name = 'Johannesburg'
API_Key = 'f343ca3a5ec4f731a75ec2583844b49b'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric"


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is', data['weather'][0]['description'])
    print('Current Temperature is ', data['main']['temp'])
    print('Current Temperature feels like ', data['main']['feels_like'])
    print('Current Humidity is ', data['main']['humidity'])


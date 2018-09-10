import requests

api_key = 'ce70aedf70a7a7224b4bd422d27c4a06'

city = input('Enter a city: ')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, api_key)
res = requests.get(url).json()

temp = res['main']['temp']
print("It's {} Celcius in {}".format(temp, city.title()))

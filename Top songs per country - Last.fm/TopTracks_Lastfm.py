import requests
from pprint import pprint


api_key = '3a88eecc40a52182cac3ca21e2fee805'
query = input('Enter a country: ')
url = 'http://ws.audioscrobbler.com/2.0/?method=Geo.getTopTracks&country={}&api_key={}&format=json'.format(query, api_key)

response = requests.get(url).json()

track_list = response['tracks']['track']

for i in track_list:
    artist = i['artist']['name']
    song_name = i['name']
    rank = int(i['@attr']['rank']) + 1

    print('{}. {} - {}'.format(rank, artist, song_name))

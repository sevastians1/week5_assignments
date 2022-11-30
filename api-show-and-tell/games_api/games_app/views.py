from re import A
from django.shortcuts import render
from django.http import HttpResponse
import requests as HTTPRequest


def index(request):
    url = "https://api.rawg.io/api/platforms?key=d97752391c18424db4fad84cfc198514"

    req = HTTPRequest.get(url)

    data = req.json()

    # all_games = (games_data['results'][0]['games'])

    all_data = data['results']


    for data in all_data:
        if data['name'] == 'PC':
            print(data['games'][0]['name'])
        
    for game in data['games']:
        print(game['name'])


    # games_info = games_url.json()

    # print(games_url)

    return HttpResponse('hello')


# GET https://api.rawg.io/api/platforms?key=d97752391c18424db4fad84cfc198514
# GET https://api.rawg.io/api/games?key=d97752391c18424db4fad84cfc198514&dates=2019-09-01,2019-09-30&platforms=18,1,7
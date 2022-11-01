from django.shortcuts import render
from django.http import JsonResponse
import requests
import random
from requests_oauthlib import OAuth1
import pprint 
pp=pprint.PrettyPrinter(indent=2, depth=2)
# Create your views here.
def main_page(request):
    cat_pic="https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492__340.jpg"
    data={"1":cat_pic,
    "2":cat_pic,
    "3":cat_pic,
    "4":cat_pic,
    "5":cat_pic}
    endpoint="https://pokeapi.co/api/v2/pokemon/ditto"
    response=requests.get(endpoint)
    responseJson=response.json()
    # pp.pprint(responseJson)
    return render(request, "main_page.html", data)

def get_pokemon(request, name):
    endpoint=f"https://pokeapi.co/api/v2/pokemon/{name}"

    try:
        data={}
        responseJson=requests.get(endpoint).json()
        # responseJson=response.json()

        types_url=responseJson["types"][0]['type']['url']
        types=requests.get(types_url).json()
        # pp.pprint(types["pokemon"])
        for x in range(1, 6):
            random_int=random.randint(1,len(types["pokemon"])-5)
            current_pokemon_json=requests.get(types["pokemon"][random_int]["pokemon"]["url"]).json()
            data[str(x)]=current_pokemon_json["sprites"]["other"]["official-artwork"]["front_default"]
            # pp.pprint(data[x])
        pp.pprint(data)
        return render(request, "main_page.html", data)
    except:
        return

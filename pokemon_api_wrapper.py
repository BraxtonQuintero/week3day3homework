# Creat a python wrapper for the Pokemon API. It should take in a pokemon name and displayy the pokemon with its height and weight

import requests

res = requests.get('https://pokeapi.co/api/v2/pokemon/')
res.json()

# base_url = 'https://pokeapi.co/api/v2'
# api_method = '/pokemon/'
# name_id = 'charizard'

# api_url = f"{base_url}{api_method}{name_id}"

# res = requests.get(api_url)
# poke_data = res.json()

# poke_height = poke_data['height']

# poke_weight = poke_data['weight']

class PokemonAPI:
    
    base_url = 'https://pokeapi.co/api/v2'
    api_method = '/pokemon/'
    
    def __init__(self, pokemon):
        self.pokemon = pokemon
        
    def get(self):
        request_url = f"{self.base_url}{self.api_method}{self.pokemon}"
        res = requests.get(request_url)
        return res.json()

    def get_height(self):
        poke_data = self.get()
        height = poke_data['height']   
        return height    

    def get_weight(self):
        poke_data =self.get()
        weight = poke_data['weight']
        return weight

poke = PokemonAPI('charizard')
print(poke.get_height())
print(poke.get_weight())


# while True:
#     while True:
#         city = input(' ')
#         if city.lower() == 'done':
#             break
#         city_obj = client.get_current_weather(city)
#         my_cities.append(city_obj)
#     for city in my_cities:
#         print(city.region)
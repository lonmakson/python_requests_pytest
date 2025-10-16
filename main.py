import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER-TOKEN'
HEADER = {'Content-Type': 'application/json'}
TRAINER_ID = '39681'

request_change_name_pokemon = requests.put(url = f'{URL}/pokemons', headers = {'trainer_token': TOKEN,
                                                                               'Content-Type': 'application/json'}, json = {"pokemon_id": "401057",
                                                                                                                            "name": "oh myyy no",
                                                                                                                            "photo_id": 997})
print(request_change_name_pokemon.json())

request_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = {'trainer_token': TOKEN,
                                                                           'Content-Type': 'application/json' },json = {"name": "generate",
                                                                                                                        "photo_id": -1})
response_data_CP = request_create_pokemon.json()
pokemon_id = response_data_CP.get("id")
print(response_data_CP)

request_pokeball_pokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = {'trainer_token': TOKEN,
                                                                                          'Content-Type': 'application/json'},
                                                                                          json = {"pokemon_id": pokemon_id})
response_data_PP = request_pokeball_pokemon.json()
print(response_data_PP)

request_list_of_enemy = requests.get(url = f'{URL}/pokemons', params = {'in_pokeball': 1, 'attack': 1})
response_data_enemy = request_list_of_enemy.json()['data'][1]
enemy_id = response_data_enemy.get("id")

request_battle_pokemon = requests.post(url = f'{URL}/battle', headers = {'trainer_token': TOKEN,
                                                                        'Content-Type': 'application/json' },
                                                                        json = { "attacking_pokemon": pokemon_id,"defending_pokemon": enemy_id})
response_data_BP = request_battle_pokemon.json()
print(response_data_BP)
import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fd2f227f19e9c4d4e5c8314c96966b12'
HEADER = {'Content-Type': 'application/json'}
TRAINER_ID = '39681'


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID, 'in_pokeball':1})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'level': 5, 'sort': 'asc', 'page': 1})
    assert response_get.json()['data'][1]['is_premium'] == False

@pytest.mark.parametrize('key, value',[('is_premium', False),('trainer_name', '404TrainerNotFound'),('id','38072'), ('city', 'Lostbyte City')])

def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'level': 5, 'sort': 'asc', 'page': 1})
    assert response_parametrize.json()['data'][1][key] ==  value


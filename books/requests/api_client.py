import requests
import random


def login(client_name=None, client_email=None):
    json = {
        'client_name': client_name,
        'client_email': client_email
    }
    response = requests.get('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response


def get_token():
    num = random.randint(1, 9999999)
    json = {
        'client_name': "Andy",
        'client_email': f'valid_email{num}@email.com'
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response.json()['accessToken']

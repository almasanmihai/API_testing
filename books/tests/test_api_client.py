from books.requests.api_client import *
from random import randint


class TestApiClient:
    num = randint(1, 999999)
    client_name = 'Andy'
    client_email = f'valid_email{num}@email.com'
    response = login(client_name=client_name, client_email=client_email)

    def test_login_201(self):
        assert self.response.status_code == 201, 'status code is not ok'

    def test_login_has_token(self):
        assert 'accessToken' in self.response.json().keys(), 'token not present'

    def test_login_409(self):
        self.response= login(self.client_name, self.client_email)
        assert self.response.status_code == 409, 'status code not ok'
        assert self.response.json()['error'] == 'API client already registered. Try a diffrent email.', 'error wrong'

    def test_invalid_email(self):
        self.response = login('andy', 'abc')
        assert self.response.status_code == 400, 'status code is not ok'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'invalid email error msg'


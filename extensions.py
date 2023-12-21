# extensions.py
import requests

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        # Здесь используйте API для получения курса валют
        # Пример: https://api.exchangerate-api.com/v4/latest/USD
        # Замените URL на используемый вами API
        url = f'https://api.example.com/v1/rates?base={base}&quote={quote}'
        response = requests.get(url)

        if response.status_code != 200:
            raise APIException('Failed to fetch exchange rates')

        data = response.json()

        if 'error' in data:
            raise APIException(data['error'])

        if quote not in data['rates']:
            raise APIException(f'Currency {quote} not found')

        rate = data['rates'][quote]
        result = rate * amount
        return result

class APIException(Exception):
    def __init__(self, message):
        self.message = message

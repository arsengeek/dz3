import requests
import json

class ConventionEx(Exception):
    pass

keys = {'биткойн' : 'BTC',
        'евро' : 'EUR',
        'доллар' : 'USD'}
class API:
    @staticmethod
    def get_price(quote, base, amoute):
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        text_base = json.loads(r.content)[keys[base]]
        amoute = float(amoute)
        text = f'Цена {amoute} {quote} в {base} - {text_base * amoute}'

        return text

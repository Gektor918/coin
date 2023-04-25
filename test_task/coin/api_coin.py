import requests as req
from coinbase.wallet.client import Client
from coin.models import Crypto

# Здесь ваши ключи
client = Client('key', 'key')


def infocheck_and_create():
    
    ''' Collection of information and creation of sapices'''

    path = "https://api.coinbase.com/v2/currencies/crypto"
    crypto = req.get(path)
    crypto_json = crypto.json()

    try:
        code_and_name = [(crypto['code'], crypto['name']) for crypto in crypto_json['data']]
        code_name_price = [(elem[0],elem[1],client.get_buy_price(currency_pair=elem[0]+'-USD')['amount']) for elem in code_and_name]
        code_name_price_rates = [(elem[0],elem[1],elem[2],client.get_exchange_rates(currency=elem[0])) for elem in  code_name_price]

    except:
        pass

    try:
        for elem in code_name_price_rates:
            Crypto.objects.create(code=elem[0], name=elem[1], current_rate=elem[2], exchange_rate=elem[3])
    except:
        pass

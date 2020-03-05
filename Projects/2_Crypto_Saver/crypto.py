
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '10',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '33bfdaf8-a8e0-4d1a-8b01-e772da0295d0',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    data = data['data']
    with open('Crypto Data.txt', 'w+') as f:
        for crypto in data:
            f.write(str(crypto['name']) + '\n')
            f.write(str(crypto['symbol']) + '\n')
            f.write(str(crypto['quote']['USD']['price']) + '\n\n')

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

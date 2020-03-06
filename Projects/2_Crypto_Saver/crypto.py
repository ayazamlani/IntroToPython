# import requests and json
import requests
import json

# get the page information
page = requests.get('https://blockchain.info/ticker')

# load the text into json format
data = json.loads(page.text)

# parse what you need
buy_price = data['USD']['buy']

# format nicely
print(f'The price of bitcoin is {buy_price}')

# write to file
with open('Bitcoin Buy Price.txt', 'w+') as f:
    f.write(f'The price of bitcoin is {buy_price}')

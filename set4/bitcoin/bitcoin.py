import requests
import json
import sys

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    print(json.dumps(r.json(), indent=2))
except requests.RequestException:
    print(f'Error in status code your status is {r.status_code}')

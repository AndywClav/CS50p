import requests
import sys

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    print(r.json())
except requests.RequestException:
    print(f'Error in status code your status is {r.status_code}')

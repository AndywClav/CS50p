import requests
import sys

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if r.status_code == 200:
        print(r.json())
except requests.RequestException:
    print("Error")

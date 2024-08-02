import requests
import json
import sys

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if len(sys.argv) < 1:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r.json(), indent=2))
except requests.RequestException:
    print(f'Error in status code your status is {r.status_code}')

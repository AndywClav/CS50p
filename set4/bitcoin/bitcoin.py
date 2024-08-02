import requests
import json
import sys

def path(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r
    except requests.RequestException:
        print(f'Error in status code your status is {r.status_code}')



if len(sys.argv) > 1:
    try:
        value_btc = sys.argv[2]
        if float(value_btc):
            print(json.dumps(r.json(), indent=2))
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

def main():


if __name__ == '__main__':
    main():

import requests
import json
import sys

def fetch_data(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raises an HTTPError for bad responses
        return r
    except requests.RequestException as e:
        print(f'Error fetching data: {e}')
        sys.exit(1)


def value_btc(json_data):
    if len(sys.argv) > 1:
        try:
            value_btc = sys.argv[1]
            if float(value_btc):
                print(json.dumps(json_data.json(), indent=2)) # You need finished the logic here, is convert the json in value current
                amount = 00000000000
                print(f"${amount:,.4f}")
        except:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)


def main():
    json_data = fetch_data('https://api.coindesk.com/v1/bpi/currentprice.json')
    value_btc(json_data)


if __name__ == "__main__":
    main()

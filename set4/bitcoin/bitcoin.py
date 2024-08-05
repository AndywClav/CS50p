import requests
import json
import sys

def fetch_data(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r
    except requests.RequestException as e:
        print(f'Error fetching data: {e}')
        sys.exit(1)


def process_value(json_data):
    if len(sys.argv) > 1:
        try:
            value_btc = sys.argv[1]
            btc_value = float(value_btc)
            data = json_data.json()
            usd_rate = float(data["bpi"]["USD"]["rate"].replace(',', ''))
            amount = btc_value * usd_rate
            
            # print(json.dumps(data, indent=2))
            print(f"${amount:,.4f}")
        except ValueError:
            print("Command-line argument is not a valid number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)


def main():
    json_data = fetch_data('https://api.coindesk.com/v1/bpi/currentprice.json')
    process_value(json_data)


if __name__ == "__main__":
    main()

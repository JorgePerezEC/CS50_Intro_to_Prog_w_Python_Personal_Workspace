import requests
import sys
import json

while True:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        cant_bit = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # print(json.dumps(response.json(), indent=2))
        o = response.json()
        usd_rate = o["bpi"]["USD"]["rate_float"]
        usd_rate = usd_rate * cant_bit
        # print("$"+str(usd_rate))
        print(f"${usd_rate:,}")
        sys.exit()
    except requests.RequestException:
        print("Null url")
    except ValueError:
        sys.exit("Command-line argument is not a number")

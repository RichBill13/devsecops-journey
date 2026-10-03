import json
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit()

    try:
        number = float(sys.argv[1])
        if number < 0:
            raise ValueError()

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        # sending the requests
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=cef6660f78b4220786a6188e98bf169ab86a68480959b9f401d543a1853506ad")
        # calling the method raiseforstatus for http error
        response.raise_for_status()
        # converting in json
        price_data = response.json()
    except requests.exceptions.HTTPError as err1:
        print(f"HTTP Error: {err1}")
        sys.exit(1)
    except requests.exceptions.ConnectionError as err2:
        print(f"connection Error: {err2}")
        sys.exit(1)
    except requests.exceptions.Timeout as err3:
        print(f"Timeout: {err3}")
        sys.exit(1)
    except requests.exceptions.RequestException as err4:
        print(f"Requests Error: {err4}") 
        sys.exit(1)


    # let's find and display the price
    try:
        bitcoin_price = float(price_data["data"]["priceUsd"])
        total_cost = number * bitcoin_price
        print(f"${total_cost:,.4f}")

    except (KeyError, TypeError, ValueError):
        print("format de donnees API invalide")
        sys.exit(1)

if __name__ == "__main__":
    main()


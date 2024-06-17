import requests

def get_crypto_price(crypto_id):
    """
    Fetch the current price of the specified cryptocurrency from CoinGecko API.
    
    Parameters:
    crypto_id (str): The CoinGecko ID of the cryptocurrency (e.g., 'bitcoin', 'ethereum')
    
    Returns:
    dict: A dictionary containing the current price and additional information
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if crypto_id in data:
            return {
                'price': data[crypto_id]['usd'],
                'currency': 'USD'
            }
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    print("Welcome to the Crypto Price Checker!")
    while True:
        crypto_id = input("Enter the cryptocurrency ID (or 'quit' to exit): ").lower()
        if crypto_id == 'quit':
            break
        price_data = get_crypto_price(crypto_id)
        if price_data:
            print(f"The current price of {crypto_id} is {price_data['price']} {price_data['currency']}.")
        else:
            print("Invalid cryptocurrency ID or unable to fetch data.")
    print("Goodbye!")

if __name__ == "__main__":
    main()

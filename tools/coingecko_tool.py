# Real-time crypto prices from CoinGecko
from langchain_core.tools import tool
import requests

@tool
def get_crypto_price(coin:str)->str:
    """Get the current price of a cryptocurrency in USD using CoinGecko."""

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin.lower()}&vs_currencies=usd"
    try:
        response=requests.get(url)
        data=response.json()
        
        if coin.lower() in data:
            price=data[coin.lower()]["usd"]
            return f"The current price of {coin.capitalize()} is ${price}"
        
        else:
            return f"Could not find price for '{coin}', Check the correct name."

    except Exception as e:
        return f"Error fetching data : {str(e)}"

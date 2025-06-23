from langchain_core.tools import tool
import requests
from utils import RAPID_API_KEY


@tool
def get_stock_price(symbol:str):
	"""Get the latest stock price from Yahoo Finance via RapidAPI"""

	url = f"https://yahoo-finance127.p.rapidapi.com/price/{symbol.upper()}"
	headers = {
		"x-rapidapi-key": RAPID_API_KEY,
		"x-rapidapi-host": "yahoo-finance127.p.rapidapi.com"}
	
	try:
		response=requests.get(url,headers=headers)
		data=response.json()
		price=data.get("regularMarketDayRange",{}).get("raw")

		if price:
			return f"The current price of {symbol.upper()} is Rs.{price}"
		else:
			return f"Could not find price for symbol '{symbol}'."

	except Exception as e:
		return f"Error:{str(e)}"

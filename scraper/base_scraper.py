# File: scraper/base_scraper.py
import requests
from datetime import datetime
from data.crypto_data import CRYPTOCURRENCIES
from data.stock_data import STOCKS
import os

my_secret = os.environ['ALPHAVANTAGE_API']

class MarketScraper:
    def __init__(self):
        self.crypto_url = "https://api.coingecko.com/api/v3/simple/price"
        self.stock_url = "https://www.alphavantage.co/query"
        self.api_key = my_secret

    def fetch_crypto_data(self):
                """
                Fetch real-time cryptocurrency data.
                """
                print("CRYPTOCURRENCIES:", CRYPTOCURRENCIES)
                symbols = ",".join([crypto["id"] for crypto in CRYPTOCURRENCIES if "id" in crypto])
                print("Constructed symbols:", symbols)

                url = "https://api.coingecko.com/api/v3/simple/price"
                params = {"ids": symbols, "vs_currencies": "usd", "include_market_cap": "true", "include_24hr_vol": "true"}

                try:
                    response = requests.get(url, params=params)
                    response.raise_for_status()
                    return response.json()
                except requests.RequestException as e:
                    print(f"Error fetching cryptocurrency data: {e}")
                    return {}


    def fetch_stock_data(self):
        market_data = []
        for stock in STOCKS:
            params = {
                "function": "TIME_SERIES_INTRADAY",
                "symbol": stock["symbol"],
                "interval": "1min",
                "apikey": my_secret
            }
            try:
                response = requests.get(self.stock_url, params=params)
                response.raise_for_status()
                data = response.json()
                time_series = data.get("Time Series (1min)", {})
                if time_series:
                    latest_time = max(time_series.keys())
                    latest_data = time_series[latest_time]
                    market_data.append({
                        "Asset Type": "Stock",
                        "Name": stock["name"],
                        "Symbol": stock["symbol"],
                        "Current Price": latest_data["1. open"],
                        "Market Cap": None,
                        "Turnover": latest_data["5. volume"],
                        "Volume 24h": None,
                        "P/E Ratio": stock.get("pe_ratio"),
                        "Timestamp": datetime.now().isoformat()
                    })
            except requests.RequestException as e:
                print(f"Error fetching stock data for {stock['symbol']}: {e}")
        return market_data

# File: main.py
import yfinance as yf
from datetime import datetime
from scraper.base_scraper import MarketScraper
from utils.write_csv import CSVManager
from analize.data_analysis import DataAnalyzer
from data.crypto_data import CRYPTOCURRENCIES
from data.stock_data import STOCKS

def fetch_stock_data(symbol_or_name):
    """
    Fetch live stock data (current price and P/E ratio) from Yahoo Finance
    given a stock symbol or name.
    """
    try:
        stock = yf.Ticker(symbol_or_name)
        stock_info = stock.info
        current_price = stock_info.get('currentPrice', None)
        pe_ratio = stock_info.get('trailingPE', None)
        
        # Return stock data in a dictionary
        return {
            "Symbol": symbol_or_name,
            "Name": stock_info.get('shortName', symbol_or_name),
            "Current Price": current_price,
            "P/E Ratio": pe_ratio,
            "Turnover": stock_info.get('regularMarketVolume', None),
            "Market Cap": stock_info.get('marketCap', None),
            "Timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        print(f"Error fetching data for {symbol_or_name}: {e}")
        return None

def main():
    scraper = MarketScraper()
    csv_manager = CSVManager()
    analyzer = DataAnalyzer()

    print("Fetching market data...")

    # Fetch cryptocurrency data
    crypto_data = scraper.fetch_crypto_data()

    # Prepare cryptocurrency data for analysis
    crypto_analysis_data = []
    for symbol, data in crypto_data.items():
        crypto_analysis_data.append({
            "Asset Type": "Crypto",
            "Name": next((crypto["name"] for crypto in CRYPTOCURRENCIES if crypto["id"] == symbol), symbol),
            "Symbol": symbol.upper(),
            "Current Price": data.get("usd", None),
            "Market Cap": data.get("usd_market_cap", None),
            "Turnover": None,
            "Volume 24h": data.get("usd_24h_vol", None),
            "P/E Ratio": None,
            "Timestamp": datetime.now().isoformat()
        })

    # Prepare stock data for analysis by fetching data from Yahoo Finance
    stock_analysis_data = []
    for symbol_or_name in STOCKS:
        stock_data = fetch_stock_data(symbol_or_name)
        if stock_data:
            stock_analysis_data.append(stock_data)

    # Analyze data and write to CSV files
    analyzer.analyze_data(crypto_analysis_data, stock_analysis_data)

if __name__ == "__main__":
    main()
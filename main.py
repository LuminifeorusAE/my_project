# File: main.py
from scraper.base_scraper import MarketScraper
from utils.write_csv import CSVManager
from analize.data_analysis import DataAnalyzer

def main():
    scraper = MarketScraper()
    csv_manager = CSVManager()
    analyzer = DataAnalyzer()

    print("Fetching market data...")
    crypto_data = scraper.fetch_crypto_data()
    stock_data = scraper.fetch_stock_data()

    combined_data = []
    for symbol, data in crypto_data.items():
        combined_data.append({
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

    combined_data.extend(stock_data)
    csv_manager.write_to_csv(combined_data)

    print("Analyzing data...")
    analyzer.analyze_data()

if __name__ == "__main__":
    main()

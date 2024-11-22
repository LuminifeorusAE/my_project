import csv
from datetime import datetime
from data.crypto_data import CRYPTOCURRENCIES
from data.stock_data import STOCKS

def scrape_market_data(output_file='data/market_data.csv'):
    """
    Scrapes market data for cryptocurrencies and stocks and writes it to a CSV file.

    :param output_file: Name of the CSV file where data will be stored.
    """
    # Placeholder for data - In a real scraper, replace this with API calls or web scraping logic
    market_data = []

    # Process cryptocurrency data
    for crypto in CRYPTOCURRENCIES:
        # Example data structure - Replace with real scraping logic
        market_data.append({
            "Asset Type": "Crypto",
            "Name": crypto["name"],
            "Symbol": crypto["symbol"],
            "Current Price": "50000",  # Mocked price
            "Market Cap": "1T",       # Mocked market cap
            "Turnover": "50B",        # Mocked turnover
            "Volume 24h": "10B",      # Mocked volume
            "P/E Ratio": None,
            "Timestamp": datetime.now().isoformat()
        })

    # Process stock data
    for stock in STOCKS:
        # Example data structure - Replace with real scraping logic
        market_data.append({
            "Asset Type": "Stock",
            "Name": stock["name"],
            "Symbol": stock["symbol"],
            "Current Price": "250",  # Mocked price
            "Market Cap": "2T",     # Mocked market cap
            "Turnover": "100B",     # Mocked turnover
            "Volume 24h": None,
            "P/E Ratio": "20",      # Mocked P/E ratio
            "Timestamp": datetime.now().isoformat()
        })

    # Write the collected data to a CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'Asset Type', 'Name', 'Symbol', 'Current Price',
            'Market Cap', 'Turnover', 'Volume 24h', 'P/E Ratio', 'Timestamp'
        ])
        writer.writeheader()
        writer.writerows(market_data)

    print(f"Market data successfully written to {output_file}")

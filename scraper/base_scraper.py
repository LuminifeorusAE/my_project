import csv
from datetime import datetime

def scrape_market_data(filename='data/market_data.csv'):
    """
    Scrapes market data (simulated here) and saves it to a CSV file.
    
    :param filename: Name of the CSV file to save the scraped data.
    """
    # Simulated data for demonstration purposes
    data = [
        {
            'Asset Type': 'Crypto',
            'Name': 'Bitcoin',
            'Symbol': 'BTC',
            'Current Price': '37500',
            'Market Cap': '725B',
            'Turnover': '5B',
            'Volume 24h': '45B',
            'P/E Ratio': None,
            'Timestamp': datetime.now().isoformat()
        },
        {
            'Asset Type': 'Stock',
            'Name': 'Tesla',
            'Symbol': 'TSLA',
            'Current Price': '240',
            'Market Cap': '700B',
            'Turnover': '1B',
            'Volume 24h': None,
            'P/E Ratio': '35.2',
            'Timestamp': datetime.now().isoformat()
        }
    ]
    
    # Define the headers for the CSV file
    headers = ['Asset Type', 'Name', 'Symbol', 'Current Price', 
               'Market Cap', 'Turnover', 'Volume 24h', 'P/E Ratio', 'Timestamp']

    # Write data to the CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"Market data successfully scraped and saved to {filename}")


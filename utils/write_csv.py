# File: utils/write_csv.py
import csv

class CSVManager:
    def __init__(self, filename='market_data.csv'):
        self.filename = filename

    def write_to_csv(self, data):
        headers = ['Asset Type', 'Name', 'Symbol', 'Current Price', 
                   'Market Cap', 'Turnover', 'Volume 24h', 'P/E Ratio', 'Timestamp']

        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print(f"Data successfully written to {self.filename}")

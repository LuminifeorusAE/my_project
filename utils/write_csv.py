# File: utils/write_csv.py
import csv
import os

class CSVManager:
    def __init__(self, file_path='data/market_data.csv'):
        self.file_path = file_path

    def write_to_csv(self, data):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        # Write data to the CSV file
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            print(f"Data successfully written to {self.file_path}")
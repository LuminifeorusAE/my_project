# File: analize/data_analysis.py
import pandas as pd

class DataAnalyzer:
    def __init__(self, csv_file='market_data.csv'):
        self.csv_file = csv_file

    def analyze_data(self):
        try:
            data = pd.read_csv(self.csv_file)
            data['Recommendation'] = data.apply(self.analyze_row, axis=1)
            print(data[['Name', 'Symbol', 'Current Price', 'Recommendation']])
        except FileNotFoundError:
            print(f"Error: {self.csv_file} not found.")

    @staticmethod
    def analyze_row(row):
        # Simplified analysis logic
        if row['Turnover'] and float(row['Turnover']) > 1_000_000:
            return "Buy"
        elif row['Turnover'] and float(row['Turnover']) > 500_000:
            return "Hold"
        else:
            return "Sell"

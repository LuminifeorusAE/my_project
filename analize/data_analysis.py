import pandas as pd

class DataAnalyzer:
    def __init__(self):
        pass

    def analyze_data(self, crypto_data, stock_data):
        # Analyze cryptocurrency data
        crypto_df = pd.DataFrame(crypto_data)
        crypto_df['Recommendation'] = crypto_df.apply(self.analyze_row, axis=1)
        crypto_df.to_csv('data/analyzed_crypto_data.csv', index=False)
        print("Analyzed crypto data saved to data/analyzed_crypto_data.csv")

        # Analyze stock data
        stock_df = pd.DataFrame(stock_data)
        stock_df['Recommendation'] = stock_df.apply(self.analyze_row, axis=1)
        stock_df.to_csv('data/analyzed_stock_data.csv', index=False)
        print("Analyzed stock data saved to data/analyzed_stock_data.csv")

    @staticmethod
    def analyze_row(row):
        # Simplified analysis logic based on 'Turnover' or 'P/E Ratio'
        if row['Turnover'] and float(row['Turnover']) > 1_000_000:
            return "Buy"
        elif row['Turnover'] and float(row['Turnover']) > 500_000:
            return "Hold"
        else:
            return "Sell"
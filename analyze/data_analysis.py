        import pandas as pd

        def analyze_market_data(input_file='data/market_data.csv', output_file='data/analyzed_data.csv'):
            """
            Analyzes market data from a CSV file and categorizes assets into Buy, Hold, or Sell.

            :param input_file: Name of the input CSV file.
            :param output_file: Name of the output CSV file with analysis results.
            """
            try:
                # Load the CSV file into a pandas DataFrame
                df = pd.read_csv(input_file)

                # Define analysis logic
                recommendations = []
                for _, row in df.iterrows():
                    if row['Asset Type'] == 'Crypto':
                        # Example: Crypto Buy signal if turnover > 10% of market cap
                        if float(row['Turnover'].replace('B', '')) / float(row['Market Cap'].replace('B', '')) > 0.1:
                            recommendations.append('Buy')
                        else:
                            recommendations.append('Hold')

                    elif row['Asset Type'] == 'Stock':
                        # Example: Stock Buy if P/E ratio < 15, Sell if > 30
                        if row['P/E Ratio'] and float(row['P/E Ratio']) < 15:
                            recommendations.append('Buy')
                        elif row['P/E Ratio'] and float(row['P/E Ratio']) > 30:
                            recommendations.append('Sell')
                        else:
                            recommendations.append('Hold')
                    else:
                        recommendations.append('Hold')

                # Add the recommendations to the DataFrame
                df['Recommendation'] = recommendations

                # Save the analyzed data back to a new CSV file
                df.to_csv(output_file, index=False)
                print(f"Analyzed data saved to {output_file}")

            except Exception as e:
                print(f"Error during analysis: {e}")

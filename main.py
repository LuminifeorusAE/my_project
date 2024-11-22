from scraper.base_scraper import scrape_market_data
from analyze.data_analysis import analyze_market_data

def main():
    # Step 1: Scrape market data
    print("Scraping market data...")
    scrape_market_data()

    # Step 2: Analyze the scraped data
    print("Analyzing market data...")
    analyze_market_data()

    print("Process complete!")

# Run the program
if __name__ == '__main__':
    main()
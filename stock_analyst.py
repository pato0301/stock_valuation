import yfinance as yf

def calculate_dividend_metrics(symbol):
    # Download historical data for the given stock symbol
    print("Getting Stock data...")
    stock_data = yf.download(symbol, start="2022-01-01", end="2023-01-01")
    print("Finish collecting stock data...")

    # Calculate Dividend Yield
    print("Calculating dividend yield...")
    dividend_yield = (stock_data['Dividends'].sum() / stock_data['Close'][-1]) * 100

    # Calculate Dividend Payout Ratio
    print("Calculating stork EPS...")
    earnings_per_share = yf.Ticker(symbol).info.get('trailingPE', None)
    print("Calculating dividend payout ratio...")
    dividend_payout_ratio = (dividend_yield / earnings_per_share) * 100 if earnings_per_share else None

    # Calculate Dividend Growth Rate
    print("Calculating dividend growth rate...")
    dividend_growth_rate = ((stock_data['Dividends'][-1] - stock_data['Dividends'][0]) / stock_data['Dividends'][0]) * 100

    # Calculate P/E Ratio
    print("Calculating stock price to share...")
    price_to_earnings_ratio = stock_data['Close'][-1] / earnings_per_share if earnings_per_share else None

    return {
        'Dividend Yield': dividend_yield,
        'Dividend Payout Ratio': dividend_payout_ratio,
        'Dividend Growth Rate': dividend_growth_rate,
        'P/E Ratio': price_to_earnings_ratio
    }

# Example: Calculate metrics for Apple Inc. (AAPL)
symbol = "AAPL"
metrics = calculate_dividend_metrics(symbol)

# Print the calculated metrics
for key, value in metrics.items():
    print(f"{key}: {value}")

import yfinance as yf
import pandas as pd

ticker_symbol = "AAPL"
print("Getting Stock data...")
ticker = yf.Ticker(ticker_symbol)
print("Finish collecting stock data...")
stock_data = ticker.history(period="max")

print(f"api ticker.info type is: {type(stock_data)}")

#print(historico_ticker)

# Function to calculate CAGR
def calculate_cagr(beginning_value, ending_value, years):
    try:
        cagr = ((ending_value / beginning_value) ** (1 / years)) - 1
        return cagr
    except ZeroDivisionError:
        print("Error: Number of years cannot be zero.")
        return None

# Number of periods ago to look back for dividends
periods_ago = 5

# Identify dates with dividends
dividend_dates = stock_data.index[stock_data['Dividends'] > 0]

# Calculate the CAGR for dividends
cagr_dividends = None

if len(dividend_dates) > 1:
    # Use the last dividend date and the earliest dividend date 5 periods ago
    latest_dividend_date = dividend_dates.max()
    dividend_periods_ago_date = latest_dividend_date - pd.DateOffset(years=5)

    latest_dividend = stock_data.loc[latest_dividend_date, 'Dividends']
    dividend_periods_ago = stock_data.loc[dividend_periods_ago_date, 'Dividends']

    # Calculate CAGR using the dividends on specific dates
    cagr_dividends = calculate_cagr(dividend_periods_ago, latest_dividend, (latest_dividend_date - dividend_periods_ago_date).days / 365)

# Print the calculated CAGR for dividends
if cagr_dividends is not None:
    print(f"CAGR for Dividends: {cagr_dividends:.2%}")
else:
    print("CAGR calculation failed.")

print(dividend_periods_ago)
import yfinance as yf
import pandas as pd

# Function to calculate CAGR
def calculate_cagr(beginning_value, ending_value, years):
    try:
        cagr = ((ending_value / beginning_value) ** (1 / years)) - 1
        return cagr
    except ZeroDivisionError:
        print("Error: Number of years cannot be zero.")
        return None


def dividend_cagr(ticker_symbol):

    # Number of periods ago to look back for dividends
    YEARS_AGO = 5
    
    ticker = yf.Ticker(ticker_symbol)
    
    try:
        dividend_dates_data = ticker.dividends
        dividend_dates_data.index = dividend_dates_data.index.strftime('%Y-%m')

        # Convert the index to datetime objects
        dividend_dates_data.index = pd.to_datetime(dividend_dates_data.index)

        # Find the closest date to today
        closest_date_today = dividend_dates_data.index.max()

        # Find the date that is 5 years ago
        five_years_ago = closest_date_today - pd.DateOffset(years=5)

        # Get the values for the closest date to today and the date that is 5 years ago
        value_today = dividend_dates_data.loc[closest_date_today]
        value_five_years_ago = dividend_dates_data.loc[five_years_ago]

        # Calculate CAGR using the dividends on specific dates
        cagr_dividends = calculate_cagr(value_five_years_ago, value_today, YEARS_AGO)

        return cagr_dividends
        
    except KeyError as e:
        print(f"Error: {e}")
        print(f"The specified timestamp {dividend_periods_ago_date} is not found in the DataFrame's index.")

# if __name__ == "__main__":
#    stock_symbol = "AAPL"
#    print(dividend_cagr(stock_symbol))
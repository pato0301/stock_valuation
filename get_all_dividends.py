import yfinance as yf
import json
import pandas as pd

def calculate_dividend_metric(ticker_symbol):
    #ticker_symbol = "SBUX"#"AAPL"
    n_years = 5
    #print("Getting Stock data...")
    stock = yf.Ticker(ticker_symbol)
    #print("Finish collecting stock data...")

    dividends_series = stock.dividends

    #print(dividends_series)

    # Step 1: Convert 'Date' column to a DateTimeIndex
    dividends_series.index = pd.to_datetime(dividends_series.index)
    #dividends_series.index += pd.TimedeltaIndex(dst_error_hours, 'h')

    # Step 2: Group by year and sum the values
    annual_dividends = dividends_series.groupby(dividends_series.index.year).sum()
    #print(annual_dividends)

    # Calculate YoY growth
    annual_dividend_growth = annual_dividends.pct_change() * 100
    #print("annual_dividend_growth: ", annual_dividend_growth)

    # Check if the data has enough years for the calculation
    if len(annual_dividend_growth) >= n_years:
        average_growth_last_n_years = annual_dividend_growth.tail(n_years).mean()
        #print(f"\nAverage Growth for the Last {n_years} Years: {average_growth_last_n_years:.2f}%")
    else:
        average_growth_last_n_years = 0
        #print(f"\nInsufficient data for calculating average growth over {n_years} years.")

    # Step 3: Check if last available year is the current year
    current_year = pd.to_datetime('today').year
    last_year = annual_dividends.index.max()

    if last_year == current_year:
        # If last available year is the current year, use the previous year
        current_year -= 1

    # Update current_year if it's greater than last_year
    if current_year > last_year:
        current_year = last_year

    # Check if the current_year - n_years is a valid year in the data
    #print("current_year: ", current_year)
    #print("last_year: ", last_year)
    #print("current_year - n_years: ", current_year - n_years)
    if (current_year - n_years) in annual_dividends.index:
        last_annual_dividend = annual_dividends.loc[last_year]
        current_minus_n_years_dividend = annual_dividends.loc[current_year - n_years]

        growth_rate = ((last_annual_dividend / current_minus_n_years_dividend) ** (1/n_years))-1

        # Print the results
        #print("Annual Dividends:")
        #print(annual_dividends)
        #print("\nGrowth Rate between Last Annual Dividend and Current Year Minus n_years (CAGR):")
        #print(growth_rate)
    else:
        #print(f"Invalid year: {current_year - n_years}")
        growth_rate =  0

    # Calculate the difference between consecutive years
    dividend_growth = annual_dividends.diff()

    # Check how many consecutive positive differences exist
    continuous_growth_years = len(dividend_growth[dividend_growth > 0])

    # Print the result
    #print(f"Number of consecutive years with dividend growth: {continuous_growth_years}")

    return continuous_growth_years, growth_rate, average_growth_last_n_years

#if __name__ == "__main__":
#    stock_symbol = "AAPL"
#    print(calculate_dividend_metric(stock_symbol))
import yfinance as yf
import json
from wacc import wacc

# This is cashflow discount

# Define the stock symbol
stock_symbol = "AAPL"

# Fetch historical stock data using yfinance
stock= yf.Ticker(stock_symbol)

# Convert the dictionary to a JSON-formatted string
#json_string = json.dumps(stock.info, indent=2)

# Convert the JSON string to a Python dictionary
#ticker_data = json.loads(json_string)

# Assumptions
fct_growth_rate = 0.03 
required_rate = wacc(stock_symbol)
# Perpetual rate at which the free cashflow is going to grow for ever, this has to be in line with the country's 
# economic growth.
perpetual_rate = 0.025
years_projected = 4
outstanding_shares = stock.info["sharesOutstanding"]

# show share count
stock_data = stock.get_shares_full(start="2020-01-01", end=None)

df_cashflow= stock.cashflow

# Order columns from oldest to newest
ordered_columns = sorted(df_cashflow.columns)

# Extract and print the values for "Free Cash Flow"
free_cash_flow_values = df_cashflow[ordered_columns].loc['Cash Flow From Continuing Operating Activities'].values.tolist()
capital_expenditure = df_cashflow[ordered_columns].loc['Capital Expenditure'].values.tolist()

# Subtract corresponding elements
free_cash_flow_to_equity = [a + b for a, b in zip(free_cash_flow_values, capital_expenditure)]
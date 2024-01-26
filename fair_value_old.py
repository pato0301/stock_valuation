import yfinance as yf
import json

# Define the stock symbol
stock_symbol = "AAPL"

# Fetch historical stock data using yfinance
stock= yf.Ticker(stock_symbol)

# Convert the dictionary to a JSON-formatted string
json_string = json.dumps(stock.info, indent=2)
#print(json_string)

# Convert the JSON string to a Python dictionary
ticker_data = json.loads(json_string)

# Calculate Dividend Yield
print("Calculating dividend yield...")
total_n_shares = stock.info["sharesOutstanding"]
#total_n_shares = ticker_data.get("floatShares", None) 

# show share count
stock_data = stock.get_shares_full(start="2022-01-01", end=None)

#print(stock_data)

# - income statement
#print(stock.income_stmt)

# - cash flow statement
#print(stock.cashflow)
df_cashflow= stock.cashflow
# Get the values of the record with the index "Free Cash Flow"
#free_cash_flow_values = df_cashflow.loc['Free Cash Flow'].values

# Print the result
#print(free_cash_flow_values)

# Order columns from oldest to newest
ordered_columns = sorted(df_cashflow.columns)

# Extract and print the values for "Free Cash Flow"
free_cash_flow_values = df_cashflow[ordered_columns].loc['Free Cash Flow'].values.tolist()
print(free_cash_flow_values)
print(type(free_cash_flow_values))


# Given free_cash_flow_values array and growth rate (fct_growth_rate)
fct_growth_rate = 0.03  # Replace this with your actual growth rate
num_periods = 5

# Initialize an array to store the results
future_values = []

# Apply the growth rate for the specified number of periods
current_value = free_cash_flow_values[-1]  # Assuming the first value in the array is the current value

for _ in range(num_periods):
    future_value = current_value * (1 + fct_growth_rate)
    future_values.append(future_value)
    current_value = future_value

# Print the result
print(future_values)

# Given future_values array, required rate (required_rate), and perpetual rate (perpetual_rate)
required_rate = 0.07  # Replace this with your actual required rate
perpetual_rate = 0.02  # Replace this with your actual perpetual rate

# Initialize an array to store the present values
present_values = []

# Calculate the present values using the formula for all values except the last one
for n, future_value in enumerate(future_values[:-1]):
    present_value = future_value / (1 + required_rate) ** (n + 1)
    present_values.append(present_value)

# Calculate the present value of the last cash flow using the specified formula
last_present_value = free_cash_flow_values[0] * ((1 + perpetual_rate) / (required_rate - perpetual_rate))

# Append the result to the present_values array
present_values.append(last_present_value)

# Print the result
print(present_values)

# Sum the values in present_values
total_present_value = sum(present_values)

# Print the result
print("instrinsic value: ", total_present_value/total_n_shares)


#print(stock.cashflow["Free Cash Flow"])

# # Fetch fundamental data using yfinance
# fundamental_data = yf.Ticker(stock_symbol).info

# # Extract relevant metrics for intrinsic value calculation
# current_price = fundamental_data["currentPrice"]
# earnings_per_share = fundamental_data["trailingEps"]
# growth_rate = fundamental_data["earningsQuarterlyGrowth"]
# discount_rate = 0.08  # You can adjust this based on your assessment of the stock's risk

# # Calculate intrinsic value using DCF formula
# intrinsic_value = earnings_per_share * (1 + growth_rate) / (discount_rate - growth_rate)

# # Print the metrics
# print(f"Stock Symbol: {stock_symbol}")
# print(f"Current Price: ${current_price:.2f}")
# print(f"Earnings per Share (EPS): ${earnings_per_share:.2f}")
# print(f"Growth Rate: {growth_rate:.2%}")
# print(f"Discount Rate: {discount_rate:.2%}")
# print(f"Intrinsic Value: ${intrinsic_value:.2f}")

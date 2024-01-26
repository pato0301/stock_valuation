import yfinance as yf
import json

ticker_symbol = "SBUX"#"AAPL"
print("Getting Stock data...")
ticker = yf.Ticker(ticker_symbol)
print("Finish collecting stock data...")

print(f"api ticker.info type is: {type(ticker.info)}")

# Convert the dictionary to a JSON-formatted string
json_string = json.dumps(ticker.info, indent=2)
#print(json_string)

# Convert the JSON string to a Python dictionary
ticker_data = json.loads(json_string)

# Calculate Dividend Yield
print("Calculating dividend yield...")
dividend_yield = ticker_data.get("dividendYield", None) * 100 if "dividendYield" in ticker_data else None

# Calculate Dividend Payout Ratio (assuming earnings per share is not provided)
trailing_pe = ticker_data.get("trailingPE", None)
print("Calculating dividend payout ratio...")
dividend_payout_ratio = (dividend_yield / trailing_pe) * 100 if dividend_yield and trailing_pe else None

# Calculate Dividend Growth Rate
print("Calculating dividend growth rate...")
earnings_growth = ticker_data.get("earningsGrowth", None)

# Calculate P/E Ratio
print("Calculating stork price to earnings...")
price_to_earnings_ratio = trailing_pe

# Additional financial metrics
total_cash = ticker_data.get("totalCash", None)
total_debt = ticker_data.get("totalDebt", None)
total_revenue = ticker_data.get("totalRevenue", None)
return_on_assets = ticker_data.get("returnOnAssets", None)
return_on_equity = ticker_data.get("returnOnEquity", None)
free_cash_flow = ticker_data.get("freeCashflow", None)

# Define thresholds for categorization
dividend_yield_threshold = 2.0  # Example: Dividend Yield above 2% is considered good
dividend_payout_ratio_threshold = 60.0  # Example: Dividend Payout Ratio below 60% is considered good
earnings_growth_threshold = 0.05  # Example: Positive earnings growth is considered good
price_to_earnings_ratio_threshold = 20.0  # Example: P/E Ratio below 20 is considered good
return_on_assets_threshold = 0.10  # Example: Return on Assets above 10% is considered good
return_on_equity_threshold = 0.15  # Example: Return on Equity above 15% is considered good
free_cash_flow_threshold = 0  # Example: Positive Free Cash Flow is considered good

# Function to categorize the metrics
def categorize_metric(value, threshold_good, threshold_great):
    if value is None:
        return "N/A"
    elif value <= threshold_great:
        return "Great"
    elif value <= threshold_good:
        return "Good"
    elif value > threshold_good:
        return "Regular"
    else:
        return "Bad"

# Function to calculate CAGR
def calculate_cagr(beginning_value, ending_value, years):
    try:
        cagr = ((ending_value / beginning_value) ** (1 / years)) - 1
        return cagr
    except ZeroDivisionError:
        print("Error: Number of years cannot be zero.")
        return None

# Calculate and categorize metrics
dividend_yield_category = categorize_metric(dividend_yield, 0, dividend_yield_threshold)
dividend_payout_ratio_category = categorize_metric(dividend_payout_ratio, dividend_payout_ratio_threshold, 100)
earnings_growth_category = categorize_metric(earnings_growth, earnings_growth_threshold, 100)
price_to_earnings_ratio_category = categorize_metric(price_to_earnings_ratio, 0, price_to_earnings_ratio_threshold)
return_on_assets_category = categorize_metric(return_on_assets, return_on_assets_threshold, 100)
return_on_equity_category = categorize_metric(return_on_equity, return_on_equity_threshold, 100)
free_cash_flow_category = categorize_metric(free_cash_flow, free_cash_flow_threshold, 100)

print("\n")
print("=====================")
print("\n")

# Print the calculated and categorized metrics
print(f"Symbol: {ticker_data['symbol']}")
print(f"Dividend Yield: {dividend_yield}% ({dividend_yield_category})")
print(f"Dividend Payout Ratio: {dividend_payout_ratio}% ({dividend_payout_ratio_category})")
print(f"Earnings Growth Rate: {earnings_growth} ({earnings_growth_category})")
print(f"P/E Ratio: {price_to_earnings_ratio} ({price_to_earnings_ratio_category})")
print(f"Return on Assets: {return_on_assets} ({return_on_assets_category})")
print(f"Return on Equity: {return_on_equity} ({return_on_equity_category})")
print(f"Free Cash Flow: {free_cash_flow} ({free_cash_flow_category})")
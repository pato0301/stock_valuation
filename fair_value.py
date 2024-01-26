import yfinance as yf
import json
from wacc import wacc

def discounted_cashflow_valuation(stock_symbol):

    # Fetch historical stock data using yfinance
    stock= yf.Ticker(stock_symbol)

    # Convert the dictionary to a JSON-formatted string
    json_string = json.dumps(stock.info, indent=2)
    #print(json_string)

    # Convert the JSON string to a Python dictionary
    ticker_data = json.loads(json_string)

    #assumptions
    fct_growth_rate = 0.03 
    required_rate = wacc(stock_symbol)
    # rate at which the free cashflow is going to grow for ever, this has to be in line with the country's 
    # economic growth.
    perpetual_rate = 0.025
    years_projected = 4

    # Calculate Dividend Yield
    #print("Calculating dividend yield...")
    outstanding_shares = stock.info["sharesOutstanding"]
    #total_n_shares = ticker_data.get("floatShares", None) 

    # show share count
    stock_data = stock.get_shares_full(start="2017-01-01", end=None)


    df_cashflow= stock.cashflow

    #print(df_cashflow)


    # Order columns from oldest to newest
    ordered_columns = sorted(df_cashflow.columns)

    # Extract and print the values for "Free Cash Flow"
    free_cash_flow_values = df_cashflow[ordered_columns].loc['Free Cash Flow'].values.tolist()
    capital_expenditure = df_cashflow[ordered_columns].loc['Capital Expenditure'].values.tolist()
    #print(free_cash_flow_values)
    #print(capital_expenditure)
    # Subtract corresponding elements
    free_cash_flow_to_equity = [a + b for a, b in zip(free_cash_flow_values, capital_expenditure)]
    #print(free_cash_flow_to_equity)

    future_free_chasflow = []
    discount_factor = []
    discount_future_free_cashflow = []


    terminal_value = free_cash_flow_values[-1] * (1 + perpetual_rate) / (required_rate - perpetual_rate)
    #print(terminal_value)

    for year in range(1,years_projected+1):
        #print(year)
        cashflow = free_cash_flow_values[-1] * (1+fct_growth_rate) ** year
        future_free_chasflow.append(cashflow)
        discount_factor.append((1+required_rate)**year)

    #print(discount_factor)
    #print(future_free_chasflow)

    for i in range(0, years_projected):
        discount_future_free_cashflow.append(future_free_chasflow[i]/discount_factor[i])

    #print(discount_future_free_cashflow)

    discounted_terminal_value = terminal_value/(1 + required_rate)**years_projected
    discount_future_free_cashflow.append(discounted_terminal_value)

    #print(discount_future_free_cashflow)

    todays_value = sum(discount_future_free_cashflow)

    #print(f"Todays value of {stock_symbol} is ${todays_value}")

    fair_value = todays_value / outstanding_shares

    #print(f"The fair value of {stock_symbol} is ${round(fair_value,2)}")

    return round(fair_value,2)

if __name__ == "__main__":
    stock_symbol = "AAPL"
    print(discounted_cashflow_valuation(stock_symbol))
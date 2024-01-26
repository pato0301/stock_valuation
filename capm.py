import yfinance as yf
import json

def capm(stock_symbol):

    # Assumption
    # We consider SP500 annual average 10% return
    MARKET_EXPENCTED_RETURN = 10

    # Define the stock symbol
    us_10year_bond_symbol = "^TNX"

    # Define the stock symbol
    #stock_symbol = "AAPL"

    # Fetch historical stock data using yfinance
    bond= yf.Ticker(us_10year_bond_symbol)

    # Fetch historical stock data using yfinance
    stock= yf.Ticker(stock_symbol)

    #print(stock.info)

    #print(stock.info["open"])

    risk_free_rate = bond.info["open"]
    beta = stock.info["beta"]

    #print(f"beta is: {beta}")
    #print(f"risk_free_rate is: {risk_free_rate}")

    capm_rate = risk_free_rate + beta * (MARKET_EXPENCTED_RETURN - risk_free_rate)

    #print(f"capm rate is: {capm_rate}")

    return capm_rate/100
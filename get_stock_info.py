import yfinance as yf
import json

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)

    # Convert the dictionary to a JSON-formatted string
    json_string = json.dumps(stock.info, indent=2)
    #print(json_string)

    # Convert the JSON string to a Python dictionary
    ticker_data = json.loads(json_string)

    print(ticker_data)

    return ticker_data


if __name__ == "__main__":
   stock_symbol = "AAPL"
   print(get_stock_data(stock_symbol))
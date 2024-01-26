import yfinance as yf
from wacc import wacc
from scrapinng_fviz import get_eps_5year_growth, get_yield_corporate_bonds_aaa

def peter_lynch_stock_value(stock_symbol):

    stock= yf.Ticker(stock_symbol)

    #variables
    future_earnings_per_share = get_eps_5year_growth(stock_symbol)
    dividend_yield = stock.info["dividendYield"] * 100
    price_to_earnings = stock.info["trailingPE"]

    print("dividend_yield: ", dividend_yield)
    print("future_earnings_per_share: ", future_earnings_per_share)
    print("price_to_earnings: ", price_to_earnings)

    # the result show you if this is over value, fairly value or under value
    intrinsic_value = (future_earnings_per_share + dividend_yield) / price_to_earnings

    status_price = ''

    if intrinsic_value < 1:
        status_price = 'over valued'
    elif intrinsic_value < 1.5:
        status_price = 'fairly valued'
    elif intrinsic_value <= 2:
        status_price = 'under valued'
    elif intrinsic_value <= 3:
        status_price = 'very under valued'
        

    return intrinsic_value, status_price


if __name__ == "__main__":
    stock_symbol = "AAPL"
    print(peter_lynch_stock_value(stock_symbol))
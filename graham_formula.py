import yfinance as yf
from scrapinng_fviz import get_eps_5year_growth, get_yield_corporate_bonds_aaa

def graham_formula(stock_symbol):

    # Fetch historical stock data using yfinance
    stock= yf.Ticker(stock_symbol)

    # Need variables
    earnings_per_share = stock.info["trailingEps"]
    price_to_earnings_no_growth = 8.5
    # growth_rate_next_5years
    g = get_eps_5year_growth(stock_symbol)
    # Current yield of AAA corporate bonds
    Y = get_yield_corporate_bonds_aaa()
    avg_yield_aaa_corporate_bonds = 4.4

    intrinsic_value = ((earnings_per_share*(price_to_earnings_no_growth + (2*g)))*avg_yield_aaa_corporate_bonds) / Y

    return round(intrinsic_value,2)

def graham_formula_revised(stock_symbol):

    # Fetch historical stock data using yfinance
    stock= yf.Ticker(stock_symbol)

    # Need variables
    earnings_per_share = stock.info["trailingEps"]
    price_to_earnings_no_growth = 7
    # growth_rate_next_5years
    g = get_eps_5year_growth(stock_symbol)
    # Current yield of AAA corporate bonds
    Y = get_yield_corporate_bonds_aaa()
    avg_yield_aaa_corporate_bonds = 4.4

    intrinsic_value = ((earnings_per_share*(price_to_earnings_no_growth + (g)))*avg_yield_aaa_corporate_bonds) / Y

    return round(intrinsic_value,2)

if __name__ == "__main__":
    stock_symbol = "AAPL"
    print(graham_formula(stock_symbol))
    print(graham_formula_revised(stock_symbol))
import yfinance as yf
from get_all_dividends import calculate_dividend_metric
from wacc import wacc

def dividend_discount_model(stock_symbol):

    # Fetch historical stock data using yfinance
    stock= yf.Ticker(stock_symbol)
    annual_dividends = stock.info["dividendRate"]
    _, _, average_growth_last_5_years = calculate_dividend_metric(stock_symbol)
    required_rate = wacc(stock_symbol)

    average_growth_last_5_years = average_growth_last_5_years / 100
   
    # Variables
    stock_price = 0
    next_year_dividend = annual_dividends * (1+average_growth_last_5_years)
    constant_cost_of_equity_capital = required_rate
    constant_growth_in_perpetuity = average_growth_last_5_years

    print("next_year_dividend: ",next_year_dividend)
    print("constant_cost_of_equity_capital: ",constant_cost_of_equity_capital)
    print("constant_growth_in_perpetuity: ",constant_growth_in_perpetuity)

    return next_year_dividend / (constant_cost_of_equity_capital - constant_growth_in_perpetuity)

if __name__ == "__main__":
    stock_symbol = "AAPL"
    print(dividend_discount_model(stock_symbol))
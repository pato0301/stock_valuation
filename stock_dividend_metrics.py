import yfinance as yf
import json
from get_all_dividends import calculate_dividend_metric 

def get_dividends_analysis_metrics(ticker_symbol):

#ticker_symbol = "SBUX"#"AAPL"
    print("Getting Stock data...")
    stock = yf.Ticker(ticker_symbol)
    print("Finish collecting stock data...")

    payout_ratio = stock.info["payoutRatio"]
    five_year_avg_dividend_yield = stock.info["fiveYearAvgDividendYield"]
    annual_dividends = stock.info["dividendRate"]
    dividend_yield = stock.info["dividendYield"]
    continuous_growth_years, five_years_dividend_growth_cagr, _ = calculate_dividend_metric(ticker_symbol)

    json_response = {
        "stock":ticker_symbol,
        "payout_ratio":payout_ratio*100,
        "five_year_avg_dividend_yield":five_year_avg_dividend_yield,
        "annual_dividends":annual_dividends,
        "dividend_yield":dividend_yield*100,
        "continuous_growth_years":continuous_growth_years
    }

    return json_response

if __name__ == "__main__":
    print(get_dividends_analysis_metrics("SBUX"))
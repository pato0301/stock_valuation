import yfinance as yf

def calculate_dividend_metrics(ticker_symbol):
    """
    Calculates key dividend metrics for a given stock ticker symbol.

    Args:
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        dict: A dictionary containing the calculated metrics.
    """

    print("Getting Stock data...")
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    financials = ticker.financials

    print("Finish collecting stock data...")
    metrics = {}

    # Dividend Yield
    print("Calculating dividend yield...")
    metrics["dividend_yield"] = info["trailingAnnualDividendYield"] * 100  # Convert to percentage

    # Dividend Growth Rate (assuming 5-year growth rate)
    print("Calculating dividend growth rate...")
    try:
        dividend_5_years_ago = financials.loc["Dividends", "5Y"]
    except KeyError:
        dividend_5_years_ago = None
        print("Dividend data not available for this ticker.")

    if dividend_5_years_ago is not None:
        metrics["dividend_growth_rate"] = ((current_dividend - dividend_5_years_ago) / dividend_5_years_ago) * 100
    else:
        metrics["dividend_growth_rate"] = None


    # Payout Ratio
    print("Calculating dividend payout ratio...")
    annual_dividends_paid = info["trailingAnnualDividendYield"] * info["regularMarketPrice"] * info["sharesOutstanding"]
    net_income = financials.loc["Net Income", "Total"]
    metrics["payout_ratio"] = (annual_dividends_paid / net_income) * 100  # Convert to percentage

    # Debt-to-Equity Ratio
    print("Calculating dividend payout ratio...")
    total_liabilities = financials.loc["Total Liabilities", "Total"]
    total_equity = financials.loc["Total Equity", "Total"]
    metrics["debt_to_equity_ratio"] = total_liabilities / total_equity

    # Earnings Per Share (EPS) Growth (assuming 5-year growth rate)
    print("Calculating stork EPS...")
    eps_5_years_ago = financials.loc["EPS", "5Y"]
    current_eps = info["trailingEps"]
    metrics["eps_growth_rate"] = ((current_eps - eps_5_years_ago) / eps_5_years_ago) * 100  # Convert to percentage

    return metrics

# Example usage
ticker_symbol = "AAPL"  # Replace with the desired ticker symbol
metrics = calculate_dividend_metrics(ticker_symbol)
print(metrics)

import streamlit as st
import pandas as pd
from get_stock_info import get_stock_data
from dividend_cagr import dividend_cagr
from fair_value import discounted_cashflow_valuation
from peter_lynch_valuation import peter_lynch_stock_value
from graham_formula import graham_formula_revised

def main():
    st.title("Stock Data App")

    # Get user input for stock ticker
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):")

    if not ticker:
        st.warning("Please enter a valid stock ticker.")
        return

    # Fetch stock data
    stock_data = get_stock_data(ticker)

    # Check if stock data is empty
    if not stock_data:
        st.warning(f"No data found for the stock ticker {ticker}. Please check the ticker symbol.")
        return

    # Extract relevant information from stock data
    price = stock_data['open']  # Example: Close price of the latest day
    annual_dividend = stock_data['dividendRate']  # Example: Replace with actual annual dividend
    dividend_yield = stock_data['dividendYield']
    pe_ratio = stock_data['trailingPE']
    ps_ratio = stock_data['priceToSalesTrailing12Months']
    price_to_growth = stock_data['trailingPegRatio']
    debt_to_equity = stock_data['debtToEquity']

    # Calculate derived metrics
    #dividend_yield = calculate_dividend_yield(price, annual_dividend)
    dividend_cagr_value = dividend_cagr(ticker)
    fair_price = discounted_cashflow_valuation(ticker)
    graham_value = graham_formula_revised(ticker)
    _, peter_lynch_value = peter_lynch_stock_value(ticker)

    # Sample data
    data = {
        'Index': [1],
        'Ticket Name': ticker,
        'Price': price,
        'Annual Dividend ': annual_dividend,
        'Dividend Yield': f"{round(dividend_yield*100,2)}%",
        'Dividend 5 CAGR': f"{round(dividend_cagr_value*100,2)}%",
        'Fair Price': fair_price,
        'Graham Value': graham_value,
        'Peter Lynch Value': peter_lynch_value,
    }

    data2 = {
        'Index': [1],
        'Ticket Name': ticker,
        'Price': price,
        'Price to Earnings (P/E)': pe_ratio,
        'P/E Status': 'Good' if (isinstance(pe_ratio, int) or isinstance(pe_ratio, float)) and pe_ratio < 20 else 'Bad',
        'Price to Sales (P/S)': ps_ratio,
        'P/S Status': 'Good' if (isinstance(ps_ratio, int) or isinstance(ps_ratio, float)) and ps_ratio >= 1 and  ps_ratio<= 2 else 'Bad',
        'Price to Growth (PEG)': price_to_growth,
        'PEG Status': 'Good' if (isinstance(price_to_growth, int) or isinstance(price_to_growth, float)) and price_to_growth < 1 else 'Bad',
        'Debt to Equity (D/E)': debt_to_equity,
        'D/E Status': 'Good' if (isinstance(debt_to_equity, int) or isinstance(debt_to_equity, float)) and debt_to_equity < 1 else 'Bad',
    }


    # Create a DataFrame
    df = pd.DataFrame(data)
    df2 = pd.DataFrame(data2)

    # Display results in a table
    st.write(f"Stock Analysis for {ticker}")
    
    # Display the table in Streamlit
    st.table(df)
    st.table(df2)
    
    # st.write("Ticket Name | Price | Annual Dividend | Dividend Yield | Dividend CAGR | Fair Price | Graham Value | Peter Lynch Value")
    # st.write(f"{ticker} | {price} | {annual_dividend} | {round(dividend_yield*100,2)}% | {dividend_cagr_value} | {fair_price} | {graham_value} | {peter_lynch_value}")

if __name__ == "__main__":
    main()

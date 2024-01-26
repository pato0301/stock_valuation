import yfinance as yf
import json
from capm import capm

def wacc(stock_symbol):

    # Define the stock symbol
    #stock_symbol = "AAPL"

    equity_rate = capm(stock_symbol)
    #print(f"equity_rate is: {equity_rate}")

    # Fetch historical stock data using yfinance
    stock= yf.Ticker(stock_symbol)

    market_cap = stock.info["marketCap"]

    # show share count
    stock_data = stock.get_shares_full(start="2022-01-01", end=None)


    df_cashflow= stock.cashflow

    #print(df_cashflow)

    df_income_stmt= stock.income_stmt

    #print(df_income_stmt)

    # Order columns from oldest to newest
    ordered_columns = sorted(df_income_stmt.columns)

    # Extract and print the values for "Free Cash Flow"
    interest_expenses = df_income_stmt[ordered_columns].loc['Interest Expense'].values.tolist()
    income_before_taxes = df_income_stmt[ordered_columns].loc['Pretax Income'].values.tolist()
    income_tax_expenses = df_income_stmt[ordered_columns].loc['Tax Provision'].values.tolist()
    #capital_expenditure = df_income_stmt[ordered_columns].loc['Capital Expenditure'].values.tolist()
    #print(interest_expenses)
    #print(income_before_taxes)
    #print(income_tax_expenses)
    tax_rate = income_tax_expenses[-1]/ income_before_taxes[-1]
    #print(f"tax rate: {tax_rate}")
    #print(df_income_stmt.index)

    # - balance sheet
    df_balance_sheet = stock.balance_sheet

    # Order columns from oldest to newest
    ordered_columns_balance_sheet = sorted(df_balance_sheet.columns)

    # Extract and print the values for "Free Cash Flow"
    long_term = df_balance_sheet[ordered_columns_balance_sheet].loc['Long Term Debt'].values.tolist()
    current_debt = df_balance_sheet[ordered_columns_balance_sheet].loc['Current Debt'].values.tolist()
    current_debt1 = df_balance_sheet[ordered_columns_balance_sheet].loc['Current Debt And Capital Lease Obligation'].values.tolist()
    long_term1 = df_balance_sheet[ordered_columns_balance_sheet].loc['Long Term Debt And Capital Lease Obligation'].values.tolist()
    total_debt = df_balance_sheet[ordered_columns_balance_sheet].loc['Total Debt'].values.tolist()

    #print(long_term)
    #print(long_term1)
    #print(current_debt)
    #print(current_debt1)
    #print("calculated total debt: ",[a + b for a, b in zip(long_term1, current_debt1)])
    #print(total_debt)


    total_amount_of_capital = market_cap + total_debt[-1]
    #print(f"total_amount_of_capital: {total_amount_of_capital}")

    total_debt_weigth = total_debt[-1] / total_amount_of_capital
    total_equity_weigth = market_cap / total_amount_of_capital
    #print(f"total_debt_weigth: {total_debt_weigth}")
    #print(f"total_equity_weigth: {total_equity_weigth}")

    cost_of_debt = interest_expenses[-1]/total_debt[-1]
    #print(f"cost_of_debt: {cost_of_debt}")

    wacc = total_debt_weigth * (cost_of_debt*(1-tax_rate)) + total_equity_weigth * equity_rate

    #print(f"wacc is: {wacc}")
    return wacc
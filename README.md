# Stock Evaluation Streamlit App

## Overview

This Streamlit app is designed to evaluate stocks based on various financial metrics and valuation models. It leverages data from financial sources and Finviz to provide insightful analysis for potential investors.

## Project Structure

The project is organized into the following working files:

- **stock_dividend_metrics**: Main script to run the Streamlit app.
- **get_all_dividends**: Module to fetch all dividends data.
- **calculate_dividend_metric**: Module to calculate dividend metrics.
- **wacc**: Module for Weighted Average Cost of Capital (WACC) calculations.
- **capm**: Module for Capital Asset Pricing Model (CAPM) calculations.
- **fair_value**: Module for discounted cash flow valuation.
- **scraping_fviz**: Module for scraping data from Finviz.
- **graham_formula**: Module for applying the Graham formula for stock valuation.
- **dividend_discount_model**: Module for the Dividend Discount Model (DDM).
- **peter_lynch_valuation**: Module for Peter Lynch's stock valuation approach.

## Python Virtual Environment

To set up a Python virtual environment for this project, run the following commands:

```bash
python -m venv stock_dividend
source stock_dividend/bin/activate  # For Linux/macOS
.\stock_dividend\Scripts\activate   # For Windows
```

## Installation

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app with the following command:

```bash
streamlit run stock_app.py
```

## Data Sources

This project relies on financial data and information from Yahoo Finance and Finviz.

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
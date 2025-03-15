import yfinance as yf
import pandas as pd

# Define the ticker symbol for OSEBX on Yahoo Finance
ticker = "OSEBX.OL"

# Fetch data (last 10 years)
osebx = yf.download(ticker, start="2015-03-01", end="2025-03-01", interval="1d")

# Save to CSV
osebx.to_csv("osebx_prices.csv")

# Show the first rows
print(osebx.head())

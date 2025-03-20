#Install yahoo Finance tool
pip install yfinance 
# Yahoo finance tool for fetching Tesla Data
import yfinance as yf 
#Pandas will be helpful for data processing
import pandas as pd 
# Define Tesla's ticker symbol
ticker_symbol = "TSLA"
# Download historical data for Tesla (Start Date , End Date and interval is 1 Day)
tesla_data = yf.download(ticker_symbol, start="2000-01-01", end="2024-03-20", interval="1d")
# Display the first few rows
print(tesla_data.head())


import pandas as pd

# Load the trade data into a data frame
trade_data = pd.read_csv('data/TradeData_5_26_2026_19_8_1.csv', encoding="iso-8859-1")

# Print out basic information
print(trade_data.info())
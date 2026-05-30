import pandas as pd

# Load the trade data into a data frame
trade_data = pd.read_csv('data/TradeData_5_26_2026_19_8_1.csv', encoding="iso-8859-1", index_col=False)

# Useful colums:
#   - refPeriodId: year for data
#   - reporterCode: country code
#   - reporterISO: country name
#   - flowCode: import/export id
#   - flowDesc: import/export name
#   - partnerCode: partner country id
#   - partnerISO: partner country name
#   - cmdCode: product code
#   - cmdDesc: product name
#   - qtyUnitCode: code for quantity unit
#   - qtyUnitAbbr: name of quantity unit
#   - qty: quantity of trade
useful_columns = ["refYear", "reporterCode", "reporterISO", "flowCode", "flowDesc", "partnerCode", "partnerISO", "cmdCode", "cmdDesc", "qtyUnitCode", "qtyUnitAbbr", "qty"]
filtered_trade_data = trade_data[useful_columns]

# Print out info
print(filtered_trade_data.info())
print(filtered_trade_data.head())
# Load environment variables for neo4j connection and pandas library for data handling
import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
from neo4j import GraphDatabase

# Initialize neo4j driver
driver = GraphDatabase.driver(
    os.getenv('NEO4J_URI'),
    auth=(
        os.getenv('NEO4J_USERNAME'), 
        os.getenv('NEO4J_PASSWORD')
    )
)

# --------- Cypher queries to load data into neo4j ----------
# Cypher query to create country nodes
create_country = """
MERGE (c:Country {id: $id, name: $name, year: $year})
"""

# Cypher query to create export resource nodes
create_resource_exports = """
MATCH (c:Country {id: $exporterId})
MERGE (c)-[:EXPORTS]->(r:Resource:Export:$($type) {id: $resourceId, type: $type, year: $year, qty: $qty})
"""

# Cypher query to create import resource nodes
create_resource_imports = """
MATCH (c:Country {id: $importerId})
MERGE (c)<-[:IMPORTS]-(r:Resource:Import:$($type) {id: $resourceId, type: $type, year: $year, qty: $qty})
"""

# Cypher query to create relationships between countries and resources
create_trade_flows = """
MATCH (export:Resource:Export {id: $exportId})
MATCH (import:Resource:Import {id: $importId})
MERGE (export)-[:FLOWS {weight: $weight}]->(import)
"""

# -------- Functions to load data into neo4j --------
def create_countries(country):
    driver.execute_query(
        create_country,
        id=country["reporterCode"],
        name=country["reporterDesc"],
        year=country["refYear"],
    )

def create_resources(resource):
    if (resource['flowCode'] == 'X'):
        create_export_resources(resource)
    elif (resource['flowCode'] == 'M'):
        create_import_resources(resource)
    else:
        print("You're not supposed to be here...")

def create_export_resources(resource):
    driver.execute_query(
        create_resource_exports,
        exporterId=resource["reporterCode"],
        resourceId=resource["resourceId"],
        type=resource["cmdDesc"],
        year=resource["refYear"],
        qty=resource["qty"],
    )

def create_import_resources(resource):
    driver.execute_query(
        create_resource_imports,
        importerId=resource["reporterCode"],
        resourceId=resource["resourceId"],
        type=resource["cmdDesc"],
        year=resource["refYear"],
        qty=resource["qty"],
    )

def create_import_flows(trade):
    driver.execute_query(
        create_trade_flows,
        exportId=trade['exportId'],
        weight=trade['qty'],
        importId=trade['importId'],
    )

# Useful colums:
#   - refPeriodId: year for data
#   - reporterCode: country code (for id)
#   - reporterDesc: country name
#   - flowCode: import/export id
#   - partnerCode: partner country id
#   - cmdCode: product code
#   - cmdDesc: product name
#   - qtyUnitCode: code for quantity unit
#   - qtyUnitAbbr: name of quantity unit
#   - qty: quantity of trade
useful_columns = ['refYear', 'reporterCode', 'reporterDesc', 'flowCode', 'partnerCode', 'cmdCode', 'cmdDesc', 'qtyUnitCode', 'qtyUnitAbbr', 'qty']

# Load the trade data into a data frame
trade_data = pd.read_csv('data/TradeData_5_31_2026_19_6_55.csv', encoding='iso-8859-1', index_col=False, usecols=useful_columns)

# ---------- Load the country nodes into neo4j ------------
country_node_columns = ['refYear', 'reporterCode', 'reporterDesc']
unique_countries = trade_data[country_node_columns].drop_duplicates()
unique_countries.apply(create_countries, axis=1)

# --------- Load the exports and imports into neo4j ----------
country_total_columns = ['refYear', 'reporterCode', 'flowCode', 'cmdCode', 'cmdDesc', 'partnerCode', 'qty']
country_totals = trade_data.loc[trade_data['partnerCode'] == 0].drop_duplicates()
country_totals['resourceId'] = country_totals['reporterCode'].astype(str) + "_" + country_totals['cmdCode'].astype(str) + "_" + country_totals['flowCode'].astype(str)
country_totals.apply(create_resources, axis=1)

# ------------ Load trade flows between partner countries into neo4j ---------------
# Get the basic pairs of data for all exporters (we will use export data, maybe in the future look at using reported imports as well)
trade_partner_columns = ['refYear', 'reporterCode', 'partnerCode', 'qty', 'flowCode', 'cmdCode']
trade_pairs = trade_data.loc[trade_data['flowCode'] == 'X', trade_partner_columns].drop_duplicates()

# Create the columns for export and import resource ids and load into neo4j
trade_pairs['exportId'] = trade_pairs['reporterCode'].astype(str) + "_" + trade_pairs['cmdCode'].astype(str) + "_X"
trade_pairs['importId'] = trade_pairs['partnerCode'].astype(str) + "_" + trade_pairs['cmdCode'].astype(str) + "_M"
trade_pairs.apply(create_import_flows, axis=1)

# Close the neo4j driver
driver.close()
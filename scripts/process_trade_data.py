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

# Cypher query to create resource nodes
create_resource = """
MERGE (c:Country {id: $exporterId})-[:EXPORTS]->(r:Resource {id: $resourceId, type: $type, year: $year, qty: $qty})
"""

# Cypher query to create relationships between countries and resources
create_import_flows = """
MERGE (r:Resource {id: $resourceId})-[:IMPORTS {weight: $weight}]->(extC:Country {id: $importerId})
"""

# -------- Functions to load data into neo4j --------
def create_countries(country):
    print(f"Loading {country["reporterDesc"]} country into Neo4j...")
    driver.execute_query(
        create_country,
        id=country["reporterCode"],
        name=country["reporterDesc"],
        year=country["refYear"],
    )

def create_resources(exporterId, resourceId, type, year, qty):
    driver.execute_query(
        create_resource,
        exporterId,
        resourceId,
        type,
        year,
        qty,
    )

def create_import_flows(resourceId, weight, importerId):
    driver.execute_query(
        create_import_flows,
        resourceId,
        weight,
        importerId,
    )

# Useful colums:
#   - refPeriodId: year for data
#   - reporterCode: country code (for id)
#   - reporterDesc: country name
#   - flowCode: import/export id
#   - flowDesc: import/export name
#   - partnerCode: partner country id
#   - partnerISO: partner country name
#   - cmdCode: product code
#   - cmdDesc: product name
#   - qtyUnitCode: code for quantity unit
#   - qtyUnitAbbr: name of quantity unit
#   - qty: quantity of trade
useful_columns = ['refYear', 'reporterCode', 'reporterDesc', 'flowCode', 'flowDesc', 'partnerCode', 'partnerISO', 'cmdCode', 'cmdDesc', 'qtyUnitCode', 'qtyUnitAbbr', 'qty']

# Load the trade data into a data frame
trade_data = pd.read_csv('data/TradeData_5_26_2026_19_8_1.csv', encoding='iso-8859-1', index_col=False, usecols=useful_columns)

# Load the country nodes into neo4j
country_node_columns = ['refYear', 'reporterCode', 'reporterDesc']
unique_countries = trade_data[country_node_columns].drop_duplicates()
unique_countries.apply(create_countries, axis=1)

# Make a list of all the relationships and resources in the trade_data table

# Load those relationships into neo4j

# Close the neo4j driver
driver.close()
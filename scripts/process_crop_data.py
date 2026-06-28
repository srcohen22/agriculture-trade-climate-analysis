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

# -------- Functions to load data into neo4j --------

# Close the neo4j driver
driver.close()
import os
from neo4j import GraphDatabase

# Initialize neo4j driver
def open_driver():
    return GraphDatabase.driver(
        os.getenv('NEO4J_URI'),
        auth=(
            os.getenv('NEO4J_USERNAME'), 
            os.getenv('NEO4J_PASSWORD')
        )
    )

# Close neo4j driver
def close_driver(driver):
    driver.close()
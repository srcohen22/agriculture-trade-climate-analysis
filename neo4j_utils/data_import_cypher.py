# --------- Cypher queries to load data into neo4j ----------

# --------- Importing Trade Flow Data -----------
# Cypher query to create country nodes
create_country = """
MERGE (c:Country {id: $id, name: $name, year: $year})
"""

# Cypher query to create export resource nodes
create_resource_exports = """
MATCH (c:Country {id: $exporterId})
MERGE (c)-[:EXPORTS]->(r:Resource:Export:$($resourceTag) {id: $resourceId, type: $type, year: $year, qty: $qty})
"""

# Cypher query to create import resource nodes
create_resource_imports = """
MATCH (c:Country {id: $importerId})
MERGE (c)<-[:IMPORTS]-(r:Resource:Import:$($resourceTag) {id: $resourceId, type: $type, year: $year, qty: $qty})
"""

# Cypher query to create relationships between countries and resources
create_trade_flows = """
MATCH (export:Resource:Export {id: $exportId})
MATCH (import:Resource:Import {id: $importId})
MERGE (export)-[:FLOWS {weight: $weight}]->(import)
"""

# --------- Importing Crop Yield Data -----------

# --------- Importing Disaster Data -----------
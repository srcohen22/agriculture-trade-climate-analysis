# These are cypher queries to be ran to ensure data is imported correctly

# ----------- General Checks -----------

# Every node except for PREV relationships should only be connected to other nodes of the same year.
invalid_temporal_relationship = """
MATCH (n)-[r]->(m) WHERE n.year <> m.year AND NOT type(r) = 'PREV' RETURN count(DISTINCT n)
"""

# ----------- Trade Flow Checks -----------



# ----------- Crop Yield Checks -----------

# ----------- Disaster Checks -----------
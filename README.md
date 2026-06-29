# Agricultural Trade & Climate Impact Knowledge Graph

A graph database for analyzing how climate-related disasters influence agricultural production and global trade networks.

Status: 🚧 Work in Progress

## About

Climate change is increasing the frequency and severity of extreme weather events, creating new risks for global agriculture and international food supply chains.

This project models the relationships between three historical datasets:

- Agricultural crop yields
- Natural disasters
- International agricultural trade

By representing these datasets in a graph database, the project aims to explore questions such as:

- Do natural disasters correlate with changes in crop yields?
- How do production shocks propagate through global trade networks?
- Which countries are most vulnerable to climate-driven supply disruptions?
- Which commodities are most sensitive to climate events?

## Architecture

### Why Graph Database?

Global trade is fundamentally a network of interconnected relationships, making graph databases a natural fit for this type of analysis.

Compared to traditional relational databases, graph databases make it significantly easier to:

- Traverse multi-country supply chains
- Analyze cascading impacts of disruptions
- Identify critical trade dependencies
- Discover highly connected countries and commodities
- Perform pathfinding and network analysis

Example research questions include:

- How does a major drought affect downstream agricultural exports?
- Which countries are most resilient to disruptions in food production?
- What are the most critical trade routes for staple crops?
- Which commodities have the highest exposure to climate risk?

## Data Sources

### Trade Data

- [UN Comtrade](https://comtradeplus.un.org/)

### Crop Yield Data

- [Food and Agriculture Organization of the United Nations (2025)](https://ourworldindata.org/grapher/yields-key-staple-crops)
    - Processed by Our World in Data

### Climate / Disaster Data

- [EM-DAT](https://data.humdata.org/dataset/emdat-country-profiles)
    - Aggregated through the Humanitarian Data Exchange (HDX)

## Graph Model

The graph models three primary domains:

- Agricultural production
- Natural disasters
- International agricultural trade

### Country Model

The following diagram illustrates how information for an individual country is represented:

![Agriculture Model Diagram](/assets/AgricultureModelDiagram.png)

### Core Nodes

- Country
- Resource
- Disaster
- Import
- Export

### Relationships

- (Country)-[:GROWS]->(Resource)
- (Country)-[:IMPACTED_BY]->(Disaster)
- (Country)-[:EXPORTS]->(Export)
- (Export)-[:TRADES]->(Import)
- (Country)-[:IMPORTS]->(Import)

### Historical Modeling

Each country node also represents a specific year.

Temporal data is connected using a PREV relationship, allowing efficient traversal across historical records without relying solely on date filtering.

This makes it easy to answer questions like:

- How has a country's agricultural production changed over time?
- How did trade relationships evolve after a major disaster?
- What long-term trends exist for a particular commodity?

![Historical Agriculture Diagram](/assets/HistoricalAgricultureDiagram.png)

### Example Queries

*Coming soon.*

Planned examples include:

- Countries most affected by drought
- Largest changes in crop yields after disasters
- Most connected agricultural exporters
- Trade dependency analysis

## Insights

*Coming soon.*

This section will document interesting correlations and insights discovered during exploration of the graph.

## Getting Started

### Requirements

- Python 3.11+
- Docker
- Neo4j

### Start Neo4j

```
make neo4j
```

### Install Dependencies

```
make init
```

### Load the Data

```
make load-trade-data
```

Additional import commands will be documented as the project grows.

## Contributing

Contributions, ideas, and feedback are always welcome.

If you're interested in graph databases, climate analytics, or agricultural economics, feel free to open an issue or submit a pull request.

## Author

Hi, I'm Sam, a software developer from Ohio.

I've been interested in climate change and global food systems for as long as I can remember. This project combines that interest with my experience in software engineering and graph databases to explore how climate events influence agricultural production and international trade.

While I don't expect this project to solve climate change, I hope it becomes a useful resource for learning, experimentation, and discussion around climate resilience and global supply chains.
# Agricultural Trade & Climate Impact Knowledge Graph

Using a graph database to analyze the impact of climate change on global agricultural trade networks.


## About

As climate change has been heating up, the world is beginning to experience more and more natural disasters and unpredictable changes. For a world as interconnected as we are now, this could spell disaster for global supply chains and food security. 

This project aims to model this reality as the interconnection between three datasets: historical crop yield, historical natural disasters, and historical trade flows. The goal is to analyze if there is any correlation between natural disasters and crop yields, and apply those learnings to global agriculture trade flows.

## Architecture

### Why Graph Database?

For modeling extremely relationship-driven datasets, such as global trade flows, graph databases provide a natural way to represent and analyze these interconnected systems. Impact analysis and pathing become trivial, whereas with a traditional tabular database it would be an extremely heavy computation.

This format lends itself naturally to answering questions such as:

- How do major droughts affect agricultural exports?
- Which countries are most vulnerable to climate-driven supply disruptions?
- How resilient are global agricultural trade networks?
- Which commodities show the highest sensitivity to climate events?

## Data Sources

### Trade Data

- [UN Comtrade](https://comtradeplus.un.org/)

### Crop Yield Data

- [Food and Agriculture Organization of the United Nations (2025)](https://ourworldindata.org/grapher/yields-key-staple-crops) (Processed by Our World in Data)

### Climate / Disaster Data

- [EM-DAT](https://data.humdata.org/dataset/emdat-country-profiles) (Aggregated by Humanitarian Data Exchange)

## Graph Model

### Core Nodes

- Country
- Resource
- Disaster
- Import
- Export

### Relationships

TODO

### Example Queries

## Interesting Outcomes

TODO

## Installation Guide

To run this, you'll just need python installed and a connection to a Neo4j container. All the necessary scripts are in the Makefile.

To start the Neo4j image in docker, you can run:
```
make neo4j
```

To install the required python libraries:
```
make init
```

To load data in the graph:
```
make load-trade-data
```

## Author

I'm Sam, a software developer from Ohio. Ever since I was a kid, I've been interested in (and quite anxious about) climate change, but I was never really sure what to do about it. Now, after working as a developer for a few years, I've gained a lot more confidence in my abilities in all aspects of software development, especially discovery and learning new things. I don't think this project will have any impact on global warming, but I hope someone out there might find it as interesting as I do.
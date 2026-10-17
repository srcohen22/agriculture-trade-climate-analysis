# Add PHONY targets
.PHONY: neo4j init load-trade-data

# install and run neo4j container
neo4j:
	docker run \
		--publish=7474:7474 --publish=7687:7687 \
		--volume=$HOME/workspace/neo4j/data:/data \
		neo4j

# install necessary packages
init:
	pip install -r requirements.txt

# load trade data into neo4j, this would only need to be done once per file
load-trade-data:
	python3 -m scripts.process_trade_data
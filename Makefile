# install and run neo4j in docker
start_neo4j := 
    docker run \
        --publish=7474:7474 --publish=7687:7687 \
        --volume=$HOME/workspace/neo4j/data:/data \
        neo4j
ARG STACK_VERSION=8.15.3

FROM docker.elastic.co/elasticsearch/elasticsearch:${STACK_VERSION}

# https://elk-docker.readthedocs.io/#installing-elasticsearch-plugins
RUN elasticsearch-plugin install --batch analysis-icu
RUN elasticsearch-plugin install --batch analysis-phonetic

# https://shunya-vichaar.medium.com/unlocking-embedding-based-search-capabilities-with-elasticsearch-and-knn-f2878907b6e3
RUN elasticsearch-plugin install --batch https://github.com/alexklibisz/elastiknn/releases/download/8.15.3.0/elastiknn-8.15.3.0.zip

RUN elasticsearch-plugin list

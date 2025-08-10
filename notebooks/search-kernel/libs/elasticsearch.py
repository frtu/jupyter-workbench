import json
from elasticsearch import Elasticsearch, helpers

class ElasticsearchClient:
    """
    A class to encapsulate Elasticsearch client functionalities.
    More info `here https://www.elastic.co/docs/reference/elasticsearch/clients/python/getting-started`__
    """

    def __init__(self, hosts: str = "http://elasticsearch:9200", max_retries: int = 5, request_timeout: int = 600):
        """
        Initializes the Elasticsearch client.

        Args:
            hosts (str): The host and port for the Elasticsearch cluster.
            max_retries (int): Maximum number of retries for a request.
            request_timeout (int): Timeout in seconds for a request.
        """
        self.es = Elasticsearch(hosts=hosts, request_timeout=request_timeout).options(max_retries=max_retries)

    def get_client(self):
        """
        Returns the Elasticsearch client instance.
        """
        return self.es

    def info(self):
        """
        Returns the Elasticsearch cluster info. Useful for sanity check.
        """
        return self.get_client().info()

    def create_index(self, index_name: str, mappings: dict):
        """
        Creates an index with the specified name and mappings if it doesn't already exist.
        More info `here https://www.elastic.co/search-labs/tutorials/search-tutorial/full-text-search/create-index`__

        Args:
            index_name (str): The name of the index to create.
            mappings (dict): The mapping for the index.
        """
        if not self.es.indices.exists(index=index_name):
            try:
                response = self.es.indices.create(index=index_name, body=mappings)
                if response.meta.status == 200:
                    print(f"Index '{index_name}' created successfully.")
                else:
                    raise RuntimeError("Failed to create index")
            except Exception as e:
                print(f"An error occurred while creating index '{index_name}': {e}")
        else:
            print(f"Index '{index_name}' already exists.")

    def delete_index(self, index_name: str):
        """
        Delete an index with the specified name.

        Args:
            index_name (str): The name of the index to create.
        """
        if self.es.indices.exists(index=index_name):
            try:
                response = self.es.indices.delete(index=index_name)
                if response.meta.status == 200:
                    print(f"Index '{index_name}' deleted successfully.")
                else:
                    raise RuntimeError("Failed to delete index")
            except Exception as e:
                print(f"An error occurred while deleting index '{index_name}': {e}")
        else:
            print(f"Index '{index_name}' doesn't exists.")

    def count_index(self, index_name: str) -> int:
        """
        Returns the number of documents in an index.

        Args:
            index_name (str): The name of the index.

        Returns:
            int: The number of documents in the index.
        """
        try:
            count = int(self.es.cat.count(index=index_name, format="json")[0]["count"])
            return count
        except Exception as e:
            print(f"An error occurred while counting documents in index '{index_name}': {e}")
            return -1

    def search_index(self, index_name: str, body: dict):
        """
        Performs a search query on the specified index.

        Args:
            index_name (str): The name of the index to search.
            body (dict): The search query body.

        Returns:
            ObjectApiResponse: The search response from Elasticsearch.
        """
        response = self.es.search(index=index_name, body=body)
        return response


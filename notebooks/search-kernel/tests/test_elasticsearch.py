from libs.elasticsearch import ElasticsearchClient
from elasticsearch.helpers import bulk
from elasticsearch.exceptions import ConnectionError
from unittest.mock import Mock, patch
import pytest

@pytest.fixture
def mock_es_client():
    """
    Fixture to create a mock ElasticsearchClient object.
    """
    with patch('libs.elasticsearch.ElasticsearchClient') as MockElasticsearch:
        mock_client = MockElasticsearch.return_value
        mock_client.options.return_value = mock_client
        
        # Mocking the .body attribute for API responses
        mock_client.info.return_value = Mock(body={'cluster_name': 'test_cluster'})
        mock_client.indices.exists.return_value = False
        mock_client.indices.create.return_value = Mock(meta=Mock(status=200))
        mock_client.cat.count.return_value = [{'count': '100'}]
        mock_client.search.return_value = Mock(body={'hits': {'total': {'value': 5}}})
        
        yield ElasticsearchClient()

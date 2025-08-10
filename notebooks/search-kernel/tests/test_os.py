from libs.os import OsUtil
import os
import pytest

@pytest.fixture(scope="module")
def setup_files(tmpdir_factory):
    """
    Fixture to create temporary files and a .env file for testing.
    """
    temp_dir = tmpdir_factory.mktemp("test_dir")
    
    # Create a dummy YAML file
    yaml_content = "api_key: 'test_yaml_key'\ncloud_id: 'test_cloud_id'\n"
    yaml_file = temp_dir.join("example_config.yml")
    yaml_file.write(yaml_content)

    # Create a dummy JSON file
    json_content = '{"name": "test_data", "value": 123}'
    json_file = temp_dir.join("example_data.json")
    json_file.write(json_content)
    
    return temp_dir

def test_load_and_get_env(setup_files, monkeypatch):
    """
    Tests if environment variables are loaded and retrieved correctly.
    """
    # Temporarily change the current working directory to the temporary directory
    monkeypatch.chdir(setup_files)

    os_util = OsUtil()
    assert os_util.get_env("NON_EXISTENT_KEY") is None
    assert os_util.get_env("NON_EXISTENT_KEY", "default_value") == "default_value"

def test_read_yaml(setup_files):
    """
    Tests if the read_yaml method correctly parses a YAML file.
    """
    file_path = str(setup_files.join("example_config.yml"))
    expected_config = {"api_key": "test_yaml_key", "cloud_id": "test_cloud_id"}
    assert OsUtil.read_yaml(file_path) == expected_config

def test_read_json(setup_files):
    """
    Tests if the read_json method correctly parses a JSON file.
    """
    file_path = str(setup_files.join("example_data.json"))
    expected_data = {"name": "test_data", "value": 123}
    assert OsUtil.read_json(file_path) == expected_data

def test_read_non_existent_file():
    """
    Tests that an error is raised for non-existent files.
    """
    with pytest.raises(FileNotFoundError):
        OsUtil.read_json("non_existent_file.json")

    with pytest.raises(FileNotFoundError):
        OsUtil.read_yaml("non_existent_file.yml")

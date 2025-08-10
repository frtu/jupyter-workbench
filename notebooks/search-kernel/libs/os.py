import os
from dotenv import load_dotenv
from getpass import getpass

import json
import yaml

class OsUtil:
    """
    A utility class for handling OS-related operations such as
    loading environment variables and reading different file formats.
    """

    def __init__(self, dotenv_path: str = None):
        """
        Initializes the OsUtil and loads environment variables from a .env file.
        
        Args:
            dotenv_path (str, optional): The path to the .env file. 
                                         Defaults to None, which loads the .env file 
                                         from the current directory.
        """
        load_dotenv(dotenv_path)

    def get_env(self, key: str, default: any = None, interactive: bool = True):
        """
        Retrieves an environment variable.
        
        Args:
            key (str): The name of the environment variable.
            default (any, optional): A default value to return if the key is not found.
                                     Defaults to None.
        
        Returns:
            str: The value of the environment variable.
        """
        response = os.getenv(key, default)
        if not response and interactive:
            response = getpass(f"Enter ENV value for {key} :")
        return response

    @staticmethod
    def read_json(file_path: str) -> dict:
        """
        Reads a JSON file and returns its content as a dictionary.
        
        Args:
            file_path (str): The path to the JSON file.
        
        Returns:
            dict: The content of the JSON file.
        """
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    @staticmethod
    def read_yaml(file_path: str) -> dict:
        """
        Reads a YAML file and returns its content as a dictionary.
        
        Args:
            file_path (str): The path to the YAML file.
        
        Returns:
            dict: The content of the YAML file.
        """
        with open(file_path, "r") as file:
            config = yaml.safe_load(file)
        return config

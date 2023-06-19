
import os
from colorama import Fore

from src.codevecdb.singleton import Singleton


class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self) -> None:
        """Initialize the Config class"""
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.milvus_uri = os.getenv("milvus_uri")
        self.milvus_user = os.getenv("milvus_user")
        self.milvus_password = os.getenv("milvus_password")
        self.milvus_collection_ttl = os.getenv("milvus_collection_ttl")
        self.milvus_collection_name = os.getenv("milvus_collection_name")
        self.milvus_collection_dim = os.getenv("milvus_collection_dim")
        self.chunk_size = int(os.getenv("chunk_size")) if os.getenv("chunk_size") else 1000
        self.chunk_overlap = int(os.getenv("chunk_overlap")) if os.getenv("chunk_overlap") else 0
        self.temperature = float(os.getenv("temperature"))
        self.module = os.getenv("module")
        self.openai_key_pool = os.getenv("OPENAI_KEY_POOL")
        self.milvus_distance = float(os.getenv("milvus_distance")) if os.getenv("milvus_distance") else 1
        self.milvus_host = os.getenv("milvus_host")
        self.milvus_port = os.getenv("milvus_port")

    def set_openai_api_key(self, value: str) -> None:
        self.openai_api_key = value

    def set_milvus_uri(self, value: str) -> None:
        self.milvus_uri = value

    def set_milvus_user(self, value: str) -> None:
        self.milvus_user = value

    def set_milvus_password(self, value: str) -> None:
        self.milvus_password = value

    def set_milvus_collection_ttl(self, value: str) -> None:
        self.milvus_collection_ttl = value


    def set_milvus_collection_name(self, value: str) -> None:
        self.milvus_collection_name = value

    def set_milvus_collection_dim(self, value: str) -> None:
        self.milvus_collection_dim = value

    def set_temperature(self, value: float) -> None:
        self.temperature = value

    def set_module(self, value: str) -> None:
        self.module = value

    def set_openai_key_pool(self, value: str) -> None:
        self.openai_key_pool = value

    def set_milvus_distance(self, value: float) -> None:
        self.milvus_distance = value

    def set_milvus_host(self, value: str) -> None:
        self.milvus_host = value

    def set_milvus_port(self, value: str) -> None:
        self.milvus_port = value


def check_openai_api_key() -> None:
    """Check if the OpenAI API key is set in config.py or as an environment variable."""
    cfg = Config()
    if not cfg.openai_api_key:
        print(
            Fore.RED
            + "Please set your OpenAI API key in .env or as an environment variable."
            + Fore.RESET
        )
        print("You can get your key from https://platform.openai.com/account/api-keys")
        exit(1)
        
conf = Config()
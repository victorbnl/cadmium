"""Utility for accessing environment variables."""

from dotenv import load_dotenv
from os import environ

load_dotenv()

def get(key):
    """Get an environment variable."""

    return environ[f"CADMIUM_{key}"]

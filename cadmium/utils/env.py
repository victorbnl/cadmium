"""Utility for accessing environment variables."""

from os import environ

from dotenv import load_dotenv

load_dotenv()


def get(key):
    """Get an environment variable."""

    return environ[f"CADMIUM_{key}"]

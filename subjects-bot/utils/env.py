"""Utility for accessing environment variables."""

from dotenv import load_dotenv
from os import environ

load_dotenv()

def get(key):
    return environ[f'SUBJECTS_BOT_{key}']

"""Configuration class."""

import dataclasses
from dataclasses import dataclass

from cadmium.config.exceptions import InvalidConfigKeyError


@dataclass
class Config():

    prefix: str = '$'
    channel: int = None
    color: int = 0x0000ff
    interval: str = '* * * * *'
    message: str = "The subject is"
    mention: str = ""

    probs_verb: float = 0.5
    probs_adverb: float = 0.9
    probs_adjective: float = 0.8
    probs_second_adjective: float = 0.3
    probs_verb_step: float = 0.2

    dashboard_channel: int = None

    auto_thread_channels: int = None

    welcome_channel: int = None
    welcome_message: str = 'Welcome {mention}!'
    goodbye_message: str = 'Goodbye {mention}'

    def get(self, key):
        """Get configuration item."""

        if hasattr(self, key):
            return getattr(self, key)

        else:
            raise InvalidConfigKeyError(f"Invalid configuration item: {key}")

    def set(self, key, value):
        """Set configuration item."""

        if hasattr(self, key):
            setattr(self, key, value)

        else:
            raise InvalidConfigKeyError(f"Invalid configuration item: {key}")

    def to_dict(self):
        """Get configuration items as a dictionary."""

        return dataclasses.asdict(self)

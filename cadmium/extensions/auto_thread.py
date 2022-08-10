"""Automatically create threads to comment under people's creations."""

import discord.utils

from cadmium.i18n import i18n
from cadmium.utils import config

def check(message):
    """Validate check if message is in right category and not an excluded channel."""

    return str(message.channel.id) in config.get("auto_thread_channels")

async def on_message(message):
    """Create threads under each message."""

    # Check
    if check(message):

        # Thread name
        if len(message.content) > 0:
            name = (
                discord.utils.remove_markdown(message.clean_content)
                .lower()
                .strip()[0:30]
            )
        else:
            name = message.attachments[0].filename
        name += f" ({i18n('comments')})"

        # Create thread
        await message.create_thread(name=name.capitalize())

def setup(bot):
    bot.add_listener(on_message)

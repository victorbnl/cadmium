"""Dashboard for managing lists."""

import discord.errors

from cadmium import config, lists
from cadmium.i18n import i18n


class Dashboard():

    def __init__(self, bot):
        super().__init__()

        self.bot = bot
        self.channel_id = int(config.get("dashboard_channel"))

        # Message
        self.message_id = None
        # Load message id
        try:
            with open("data/dashboard_message_id.txt", "r") as file_:
                id = int(file_.read())
                # Id exists in file
                if id:
                    self.message_id = id
        # No message file
        except FileNotFoundError:
            pass

    async def update(self):
        # Content
        content = ("\n\n".join(
            "\n".join(
                (
                    f"**__{i18n(f'lists.{lst}').capitalize()}__**",
                    ", ".join(
                        f"`{word}`"
                        for word in getattr(lists, lst).items()
                    )
                )
            )
            for lst in ('noun', 'verb', 'adjective', 'adverb')
        ))

        # Get channel
        channel = self.bot.get_channel(self.channel_id)

        # Message already exists
        if self.message_id:
            # Get message
            try:
                message = await channel.fetch_message(self.message_id)
                # Edit it
                if message:
                    await message.edit(content=content)
                    return
            except discord.errors.NotFound:
                pass

        # Message doesn't exist
        await channel.purge()
        # Create it
        message = await self.bot.get_channel(self.channel_id).send(content)
        self.message_id = message.id
        # Save it
        with open("data/dashboard_message_id.txt", "w") as file_:
            file_.write(str(self.message_id))

    async def on_ready(self):
        await self.update()

    async def on_message(self, message):

        # Check if message has been sent in dashboard and is not the bot's one
        if (
            message.channel.id == self.channel_id
            and message.author.id != self.bot.user.id
        ):

            # Parse and delete message
            parsed = message.content.split()
            await message.delete()

            # If first word is a command
            if parsed[0] in (
                "noun",
                "nouns",
                "verb",
                "verbs",
                "adjective",
                "adjectives",
                "adverb",
                "adverbs"
            ):

                # Support both singular and plural
                list_ = parsed[0]
                singular = {
                    'nouns': 'noun',
                    'verbs': 'verb',
                    'adjectives': 'adjective',
                    'adverbs': 'adverb'
                }
                if list_ in singular.keys():
                    list_ = singular[list_]
                list_ = getattr(lists, list_)

                words = parsed[1:]

                # Add or remove each word
                with lists.db.atomic():
                    for word in words:
                        list_.update(word)

                # Update dashboard message
                await self.update()


def setup(bot):

    dashboard = Dashboard(bot)

    bot.add_listener(dashboard.on_message)
    bot.add_listener(dashboard.on_ready)

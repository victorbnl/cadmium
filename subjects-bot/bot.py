"""The bot."""

import discord
from discord.ext import commands

import discord_send_embed

from discord_simple_pretty_help import SimplePrettyHelp

import subject
import artwork

from utils import config

intents = discord.Intents.default()
intents.message_content = True

class SubjectsBot(commands.Bot):
    """The main bot class."""

    async def block_other_guilds_check(self, ctx):
        """Checks if the command has been sent in the correct guild and by the correct role"""

        role = discord.utils.find(lambda r: r.id == self.role_id, ctx.guild.roles)
        return ctx.guild.id == self.guild_id and role in ctx.author.roles

    def __init__(self, guild_id, role_id, prefix, color):
        """Initialize the bot."""

        super().__init__(
            command_prefix=prefix,
            intents=intents,
            help_command=SimplePrettyHelp(color=color)
        )

        self.guild_id = guild_id
        self.role_id = role_id

        self.add_check(self.block_other_guilds_check)

        for ext in ("manage_lists", "admin", "error"):
            self.load_extension(f"extensions.{ext}")
            print(f"Loaded extension {ext}")

    async def send_subject(self):
        """Sends a subject. Function to be called at every interval and by the trigger command."""

        channel_id = int(config.get("channel").replace("<#", "").replace(">", ""))
        message = config.get("message")
        todays_subject = subject.get_subject()

        channel = self.get_channel(channel_id)

        image = artwork.subject_banner(message, todays_subject)

        await channel.send(file=discord.File(fp=image, filename="subject.jpg"))
    
    def reschedule_job(self):
        """Reschedules the job, to be ran after a change of interval."""

        raise NotImplementedError

    async def on_ready(self):
        """When the bot starts."""

        print("Ready!")

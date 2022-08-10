"""The bot."""

import discord
from discord.ext import commands

from discord_simple_pretty_help import SimplePrettyHelp

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from cadmium.utils import config

from cadmium.get_subject import get_subject

# Intents required for interacting with messages
intents = discord.Intents.default()
intents.message_content = True

class Cadmium(commands.Bot):
    """The main bot class."""

    async def block_other_guilds_check(self, ctx):
        """Checks if the command has been sent in the correct guild and by the correct role."""

        role = discord.utils.find(lambda r: r.id == self.role_id, ctx.guild.roles)
        return ctx.guild.id == self.guild_id and role in ctx.author.roles

    def __init__(self, guild_id, role_id, prefix, color):
        """Initialize the bot."""

        super().__init__(
            command_prefix=prefix,
            intents=intents,
            help_command=SimplePrettyHelp(color=color),
        )

        # Command check
        self.guild_id = guild_id
        self.role_id = role_id
        self.add_check(self.block_other_guilds_check)

        # Load extensions (cogs)
        for ext in ("admin", "dashboard", "error", "test", "auto_thread"):
            self.load_extension(f"cadmium.extensions.{ext}")
            print(f"Loaded extension {ext}")

    async def send_subject(self):
        """Sends a subject. Function to be called at every interval and by the trigger command."""

        # Channel
        channel_id = int(config.get("channel").replace("<#", "").replace(">", ""))
        channel = self.get_channel(channel_id)

        image = get_subject()

        # Send subject
        await channel.send(
            content=config.get("mention"),
            file=discord.File(fp=image, filename="subject.jpg"),
        )

    def reschedule_job(self):
        """Reschedules the job, to be ran after a change of interval."""

        raise NotImplementedError

    async def on_ready(self):
        """Sets up the scheduler."""

        # Create the scheduler used to send subject each `interval`
        scheduler = AsyncIOScheduler()
        scheduler.add_job(
            self.send_subject,
            CronTrigger.from_crontab(config.get("interval")),
            id="send_subject",
        )
        scheduler.start()

        print("Ready!")

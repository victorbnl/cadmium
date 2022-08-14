import discord
from discord.ext import commands
from discord_simple_pretty_help import SimplePrettyHelp

from cadmium import scheduler, get_subject, config


intents = discord.Intents.default()
intents.message_content = True


class CadmiumBot(commands.Bot):

    def __init__(
        self,
        guild_id,
        role_id
    ):
        """The Cadmium Discord bot."""

        super().__init__(
            command_prefix=config.get('prefix'),
            intents=intents,
            help_command=SimplePrettyHelp(),
        )

        # Subjects channel
        self.channel_id = int(config.get('channel'))

        # Mention
        self.mention = config.get('mention')

        # Command check

        self.guild_id = int(guild_id)
        self.role_id = int(role_id)

        def check(ctx):
            return (
                ctx.guild.id == self.guild_id
                and self.role_id in [role.id for role in ctx.author.roles]
            )

        self.add_check(check)

        # Load extensions
        for ext in (
            'dashboard', 'test', 'config', 'auto_thread', 'error', 'admin'
        ):
            print(f"Loading extension {ext}")
            self.load_extension(f'cadmium.extensions.{ext}', store=False)

    async def on_ready(self):
        """When the bot is ready."""

        # Fetch channel
        self.channel = self.get_channel(self.channel_id)

        # Schedule subject sending
        scheduler.schedule(self.send_subject, config.get('interval'))

        print("Ready")

    async def send_subject(self, channel_id=None):
        """Generate and send a subject."""

        # Fetch channel if channel id provided
        channel = self.channel
        if channel_id:
            channel = self.get_channel(channel_id)

        # Get subject banner
        banner = get_subject.get_subject()

        # Send it
        await channel.send(
            content=self.mention,
            file=discord.File(fp=banner, filename="subject.jpg")
        )

"""Say welcome and goodbye to users."""

from cadmium import config


class Welcome():

    def __init__(self, bot):
        self.bot = bot

    async def send_message(self, member, message):
        """Send a message in the welcome channel."""

        # Get channel
        channel_id = int(config.get('welcome_channel'))
        channel = self.bot.get_channel(channel_id)

        # Format message
        message = message.format(
            mention=member.mention,
            name=member.name
        )

    async def on_member_join(self, member):
        """When a member joins the server."""

        await self.send_message(member, config.get('welcome_message'))

    async def on_member_remove(self, member):
        """When a member leaves the server."""

        await self.send_message(member, config.get('goodbye_message'))


def setup(bot):

    welcome = Welcome(bot)

    bot.add_listener(welcome.on_member_join)
    bot.add_listener(welcome.on_member_remove)

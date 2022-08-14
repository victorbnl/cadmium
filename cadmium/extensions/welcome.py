"""Say welcome and goodbye to users."""

from cadmium import config


class Welcome():

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        """When a member joins the server."""

        channel_id = int(config.get('welcome_channel'))
        channel = self.bot.get_channel(channel_id)
        message = config.get('welcome_message').format(mention=member.mention)
        await channel.send(message)

    async def on_member_remove(self, member):
        """When a member leaves the server."""

        channel_id = int(config.get('welcome_channel'))
        channel = self.bot.get_channel(channel_id)
        message = config.get('goodbye_message').format(mention=member.mention)
        await channel.send(message)


def setup(bot):

    welcome = Welcome(bot)

    bot.add_listener(welcome.on_member_join)
    bot.add_listener(welcome.on_member_remove)

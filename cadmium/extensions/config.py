"""Commands for getting and setting configuration items."""

from typing import Optional

import discord
from discord.ext import commands

from cadmium import config
from cadmium.i18n import i18n


class Config(
    commands.Cog,
    name=i18n('cogs.config.name'),
    description=i18n('cogs.config.description')
):

    @commands.command(
        brief=i18n('commands.config.brief'),
        extras={
            'args': {
                'key': i18n('commands.config.args.key'),
                'value': i18n('commands.config.args.value'),
            }
        },)
    async def config(self, ctx, key: Optional[str], *values):

        # Key is none -> get full configuration
        if key is None:
            message = "\n".join(
                f"`{key}`: {value}" for key, value in config.to_dict().items()
            )

        # No values but a key -> get config parameter
        elif len(values) == 0:
            value = config.get(key)

            message = i18n(
                'messages.config_item_is', {'key': key, 'value': value}
            )

        # Both key and value are set -> set config parameter
        else:
            value = values[0] if len(values) == 1 else list(values)
            config.set(key, value)

            message = i18n(
                'messages.config_item_set_to', {'key': key, 'value': value}
            )

        # Send what has been done
        await ctx.send(embed=discord.Embed(description=message))


def setup(bot):
    bot.add_cog(Config(bot))

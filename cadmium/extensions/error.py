"""Displays command errors in a nice red embed."""

import discord

from cadmium.i18n import i18n


async def on_command_error(ctx, error):
    """Command error handler"""

    # Send error message
    await ctx.send(
        embed=discord.Embed(
            title=i18n('error'),
            description=error,
            color=0xFF0000
        )
    )


def setup(bot):
    bot.add_listener(on_command_error)

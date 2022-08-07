"""Displays command errors in a nice red embed."""

import discord


async def on_command_error(ctx, error):
    """Command error handler"""

    # Send error message
    await ctx.send(
        embed=discord.Embed(title="Error", description=error, color=0xFF0000)
    )


def setup(bot):
    bot.add_listener(on_command_error)

#-*- coding: utf-8 -*-

import discord
from discord.ext import commands

async def on_command_error(ctx, error):
    """Command error handler"""

    await ctx.send_embed({
        "title": "Error",
        "description": error,
        "color": 0xFF0000
    })

def setup(bot):
    bot.add_listener(on_command_error)

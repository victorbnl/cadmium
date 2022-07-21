#-*- coding: utf-8 -*-

import discord
from discord.ext import commands


async def on_command_error(ctx, error):
    """Command error handler"""
    
    embed = discord.Embed(
        colour=0xFF0000,
        title="Error",
        description=str(error).capitalize()
    )
    
    await ctx.send(embed=embed)


def setup(bot):
    bot.add_listener(on_command_error)

"""Set default embed color."""

import discord

from utils import config

default_send_embed = discord.abc.Messageable.send_embed
async def send_embed(self, embed_dict, **kwargs):
    if "color" not in embed_dict.keys():
        embed_dict["color"] = int(config.get("color"), 16)
    return await default_send_embed(self, embed_dict, **kwargs)
discord.abc.Messageable.send_embed = send_embed

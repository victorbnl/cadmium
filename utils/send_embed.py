#!/usr/bin/env python3

import discord

import utils.config as config

async def send_embed(self, dict_):
    
    embed = discord.Embed.from_dict(dict_)
    await self.send(embed=embed)

discord.abc.Messageable.send_embed = send_embed

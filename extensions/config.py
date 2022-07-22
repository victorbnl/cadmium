#-*- coding: utf-8 -*-

import discord
from discord.ext import commands
import typing

import utils.config as config


class Config(commands.Cog, name="Configuration"):


    @commands.command(
        brief="Définir ou afficher des paramètres",
        extras={
            "args": {
                "key": "propriété à définir ou afficher (\"channel\", \"message\", \"frequency\")",
                "value": "valeur sur laquelle la configurer"
            }
        }
    )
    async def config(self, ctx, key: typing.Literal["channel", "message", "frequency"], *, value: typing.Optional[str]):
        if value is None:
            value = config.get(key)
            message = "{} est {}".format(key.capitalize(), value)
        else:
            config.set(key, value)
            message = "{} a été défini sur {}".format(key.capitalize(), value)
        
        embed = discord.Embed(
            colour = 0x595959,
            description=message
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Config(bot))

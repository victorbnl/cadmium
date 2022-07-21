#-*- coding: utf-8 -*-

from discord.ext import commands
import typing

import utils.config as config


class Config(commands.Cog, name="Configuration"):


    @commands.command(
        brief="Définir ou afficher des paramètres",
        extras={
            "args": {
                "key": "propriété à définir ou afficher (\"channel\", \"message\")",
                "value": "valeur sur laquelle la configurer"
            }
        }
    )
    async def config(self, ctx, key: typing.Literal["channel", "message"], *, value: typing.Optional[str]):
        if value is None:
            value = config.get(key)
            await ctx.send("{} is {}".format(key.capitalize(), value))
        else:
            config.set(key, value)
            await ctx.send("{} set to {}".format(key.capitalize(), value))


def setup(bot):
    bot.add_cog(Config(bot))

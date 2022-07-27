#-*- coding: utf-8 -*-

import discord
from discord.ext import commands
import typing

import yaml

import utils.config as config

class Config(commands.Cog, name="Administration"):

    @commands.command(
        brief="Définir ou afficher des paramètres de configuration",
        extras={
            "args": {
                "key": "propriété à définir ou afficher (\"channel\", \"message\", \"frequency\")",
                "value": "valeur sur laquelle la configurer"
            }
        }
    )
    async def config(self, ctx, key: typing.Optional[str], *, value: typing.Optional[str]):
        if key is None:
            configuration = config.get_config()
            
            def walk_conf(dict_=configuration, i=0, opts=[]):
                for key in dict_:
                    if isinstance(dict_[key], dict):
                        opts.append(f"{'⠀'*2*i} - `{key}`:")
                        walk_conf(dict_[key], i+1, opts)
                    else:
                        opts.append(f"{'⠀'*2*i} - `{key}`: {dict_[key]}")
                return "\n".join(opts)
            
            string = walk_conf()

            message = f"**Config**\n{string}"

        elif value is None:
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
    
    @commands.command(brief="Lancer manuellement la génération d'un sujet")
    async def trigger(self, ctx):
        await ctx.bot.send_subject()

def setup(bot):
    bot.add_cog(Config(bot))

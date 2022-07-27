#-*- coding: utf-8 -*-

import discord
from discord.ext import commands
from typing import Literal

import yaml

class ManageLists(commands.Cog, name="Gérer les listes"):
    
    @commands.command(
        brief="Ajoute un mot à une liste",
        extras={
            "args": {
                "type": "nature (\"noun\", \"adjective\", \"verb\", \"adverb\")",
                "args": "mots à ajouter"
            }
        }
    )
    async def add(self, ctx, type: Literal["noun", "adjective", "verb", "adverb"], *args: str):
        with open(f"data/lists/{type}s.yml", "r+") as file_:
            items = yaml.safe_load(file_) or []
            for arg in args:
                items.append(arg)
            file_.seek(0)
            file_.write(yaml.dump(items, allow_unicode=True))
            file_.truncate()

        embed = discord.Embed(
            colour = 0x4287f5,
            description=f"Ajouté·s à la liste {type}s : {', '.join(f'`{arg}`' for arg in args)}"
        )

        await ctx.send(embed=embed)

    @commands.command(
        aliases=["rm"],
        brief="Retire un mot d'une liste",
        extras={
            "args": {
                "type": "nature (\"noun\", \"adjective\", \"verb\", \"adverb\")",
                "args": "mots à retirer"
            }
        }
    )
    async def remove(self, ctx, type: Literal["noun", "adjective", "verb", "adverb"], *args: str):
        with open(f"data/lists/{type}s.yml", "r+") as file_:
            items = yaml.safe_load(file_) or []
            for arg in args:
                items.remove(arg)
            file_.seek(0)
            file_.write(yaml.dump(items, allow_unicode=True))
            file_.truncate()

        embed = discord.Embed(
            colour = 0x4287f5,
            description=f"Retiré·s de la liste *{type}s* : {', '.join(f'`{arg}`' for arg in args)}"
        )

        await ctx.send(embed=embed)

    @commands.command(
        aliases=["ls"],
        brief="Affiche les mots d'une liste",
        extras={
            "args": {
                "type": "nature (\"noun\", \"adjective\", \"verb\", \"adverb\")"
            }
        }
    )
    async def list(self, ctx, type: Literal["noun", "adjective", "verb", "adverb"]):
        with open(f"data/lists/{type}s.yml", "r") as file_:
            items = yaml.safe_load(file_) or []
            
        embed = discord.Embed(
            colour=0x4287f5,
            title=f"{type.capitalize()}s",
            description=", ".join(f"`{item}`" for item in items)
        )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ManageLists(bot))

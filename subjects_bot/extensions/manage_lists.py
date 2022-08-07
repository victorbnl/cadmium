"""Manage the lists via bot commands."""

import discord
from discord.ext import commands
from typing import Literal

import yaml


class ManageLists(commands.Cog, name="Gérer les listes"):
    """Add, remove or list items from the word lists."""

    @commands.command(
        brief="Ajoute un mot à une liste",
        extras={
            "args": {
                "type": 'nature ("noun", "adjective", "verb", "adverb")',
                "args": "mots à ajouter",
            }
        },
    )
    async def add(
        self, ctx, type: Literal["noun", "adjective", "verb", "adverb"], *args: str
    ):
        """Adds a word to a list."""

        # Read word list
        with open(f"data/lists/{type}s.yml", "r+") as file_:
            items = yaml.safe_load(file_) or []

            # Append each word to items
            for arg in args:
                items.append(arg)

            # Write the new list
            file_.seek(0)
            file_.write(yaml.dump(items, allow_unicode=True))
            file_.truncate()

        # Send what has been done
        await ctx.send(
            embed=discord.Embed(
                description=f"Ajouté·s à la liste {type}s : {', '.join(f'`{arg}`' for arg in args)}"
            )
        )

    @commands.command(
        aliases=["rm"],
        brief="Retire un mot d'une liste",
        extras={
            "args": {
                "type": 'nature ("noun", "adjective", "verb", "adverb")',
                "args": "mots à retirer",
            }
        },
    )
    async def remove(
        self, ctx, type: Literal["noun", "adjective", "verb", "adverb"], *args: str
    ):
        """Removes a word from a list."""

        # Read word list
        with open(f"data/lists/{type}s.yml", "r+") as file_:
            items = yaml.safe_load(file_) or []

            # Remove each word
            for arg in args:
                items.remove(arg)

            # Write the new list
            file_.seek(0)
            file_.write(yaml.dump(items, allow_unicode=True))
            file_.truncate()

        # Send what has been done
        await ctx.send(
            embed=discord.Embed(
                description=f"Retiré·s de la liste *{type}s* : {', '.join(f'`{arg}`' for arg in args)}"
            )
        )

    @commands.command(
        aliases=["ls"],
        brief="Affiche les mots d'une liste",
        extras={"args": {"type": 'nature ("noun", "adjective", "verb", "adverb")'}},
    )
    async def list(self, ctx, type: Literal["noun", "adjective", "verb", "adverb"]):
        """List the words of a list."""

        # Read items
        with open(f"data/lists/{type}s.yml", "r") as file_:
            items = yaml.safe_load(file_) or []

        # Send them
        await ctx.send(
            embed=discord.Embed(
                title=f"{type.capitalize()}s",
                description=", ".join(f"`{item}`" for item in items),
            )
        )


def setup(bot):
    bot.add_cog(ManageLists(bot))

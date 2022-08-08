"""Manage the lists via bot commands."""

import discord
from discord.ext import commands
from typing import Literal

from subjects_bot.utils.lists import lists


class ManageLists(commands.Cog, name="Gérer les listes"):
    """Add, remove or list items from the word lists."""

    @commands.command(
        brief="Ajoute un mot à une liste",
        extras={
            "args": {
                "type": 'nature ("noun", "adjectives", "verbs", "adverbs")',
                "args": "mots à ajouter",
            }
        },
    )
    async def add(
        self, ctx, type: Literal["nouns", "adjectives", "verbs", "adverbs"], *words: str
    ):
        """Adds a word to a list."""

        # Add each word into the list
        for word in words:
            lists[type].add(word)

        # Send what has been done
        await ctx.send(
            embed=discord.Embed(
                description=f"Ajouté·s à la liste {type} : {', '.join(f'`{word}`' for word in words)}"
            )
        )

    @commands.command(
        aliases=["rm"],
        brief="Retire un mot d'une liste",
        extras={
            "args": {
                "type": 'nature ("nouns", "adjectives", "verbs", "adverbs")',
                "args": "mots à retirer",
            }
        },
    )
    async def remove(
        self, ctx, type: Literal["nouns", "adjectives", "verbs", "adverbs"], *words: str
    ):
        """Removes a word from a list."""

        # Remove each word from the list
        for word in words:
            lists[type].remove(word)

        # Send what has been done
        await ctx.send(
            embed=discord.Embed(
                description=f"Retiré·s de la liste *{type}* : {', '.join(f'`{word}`' for word in words)}"
            )
        )

    @commands.command(
        aliases=["ls"],
        brief="Affiche les mots d'une liste",
        extras={"args": {"type": 'nature ("nouns", "adjectives", "verbs", "adverbs")'}},
    )
    async def list(self, ctx, type: Literal["nouns", "adjectives", "verbs", "adverbs"]):
        """List the words of a list."""

        # Read items
        items = lists[type].items

        # Send them
        await ctx.send(
            embed=discord.Embed(
                title=f"{type.capitalize()}",
                description=", ".join(f"`{item}`" for item in items),
            )
        )


def setup(bot):
    bot.add_cog(ManageLists(bot))

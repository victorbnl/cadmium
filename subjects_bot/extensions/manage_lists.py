"""Manage the lists via bot commands."""

import discord
from discord.ext import commands
from typing import Literal

from subjects_bot.utils.lists import lists
from subjects_bot.i18n import i18n


class ManageLists(commands.Cog, name=i18n("cogs.manage_lists.name")):
    """Add, remove or list items from the word lists."""

    @commands.command(
        brief=i18n("commands.add.brief"),
        extras={
            "args": {
                "type": f'{i18n("commands.add.args.type")} ("noun", "adjectives", "verbs", "adverbs")',
                "words": i18n("commands.add.args.words"),
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
                description=i18n(
                    "messages.added",
                    {"list": type, "words": ", ".join(f"`{word}`" for word in words)},
                )
            )
        )

    @commands.command(
        aliases=["rm"],
        brief=i18n("commands.remove.brief"),
        extras={
            "args": {
                "type": f'{i18n("commands.remove.args.type")} ("nouns", "adjectives", "verbs", "adverbs")',
                "words": i18n("commands.remove.args.words"),
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
                description=i18n(
                    "messages.removed",
                    {"list": type, "words": ", ".join(f"`{word}`" for word in words)},
                )
            )
        )

    @commands.command(
        aliases=["ls"],
        brief=i18n("commands.list.brief"),
        extras={
            "args": {
                "type": f'{i18n("commands.list.args.type")} ("nouns", "adjectives", "verbs", "adverbs")'
            }
        },
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

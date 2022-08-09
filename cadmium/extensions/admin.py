"""Commands for administrating the bot."""

import subprocess
import typing
from sys import exit
import os.path

import discord
from discord.ext import commands

from cadmium.exceptions import *
from cadmium.i18n import i18n

from cadmium.utils import config


class Config(
    commands.Cog,
    name=i18n("cogs.admin.name"),
    description=i18n("cogs.admin.description"),
):
    """Set or get configuration parameters."""

    @commands.command(brief=i18n("commands.update.brief"))
    async def update(self, ctx):
        """Updates the bot."""

        if os.path.exists("update.sh"):
            await ctx.send(embed=discord.Embed(description=i18n("messages.updating")))
            subprocess.run(["./update.sh"])
            exit(0)

        else:
            raise MissingUpdateScriptError(i18n("messages.missing_update_script"))

    @commands.command(
        brief=i18n("commands.config.brief"),
        extras={
            "args": {
                "key": i18n("commands.config.args.key"),
                "value": i18n("commands.config.args.value"),
            }
        },
    )
    async def config(
        self, ctx, key: typing.Optional[str], *, value: typing.Optional[str]
    ):
        """Defines or shows configuration parameters."""

        # Key is none -> getting full configuration
        if key is None:
            configuration = config.get_config()

            def walk_conf(dict_=configuration, i=0, opts=[]):
                for key in dict_:
                    if isinstance(dict_[key], dict):
                        opts.append(f"{'⠀'*(2*i+1)}`{key}`:")
                        walk_conf(dict_[key], i + 1, opts)
                    else:
                        opts.append(f"{'⠀'*(2*i+1)}`{key}`: {dict_[key]}")
                return "\n".join(opts)

            string = walk_conf()

            message = f"{string}"

        # Value is None but key is not -> getting config parameter
        elif value is None:
            value = config.get(key)

            message = i18n("messages.config_item_is", {"key": key, "value": value})

        # Both key and value are set -> set config parameter
        else:
            config.set(key, value)

            message = i18n("messages.config_item_set_to", {"key": key, "value": value})

        # Send what has been done
        await ctx.send(embed=discord.Embed(description=message))

    @commands.command(brief=i18n("commands.reschedule.brief"))
    async def reschedule(self, ctx):
        """Manually reschedules the job after an interval change."""

        ctx.bot.reschedule_job()
        await ctx.send(
            i18n("messages.rescheduled_to", {"interval": config.get("interval")})
        )

    @commands.command(brief=i18n("commands.trigger.brief"))
    async def trigger(self, ctx):
        """Manually starts sending a subject."""

        await ctx.bot.send_subject()


def setup(bot):
    bot.add_cog(Config(bot))

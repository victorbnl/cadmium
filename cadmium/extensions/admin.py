"""Commands for administrating the bot."""

import typing

import discord
from discord.ext import commands

from cadmium import config
from cadmium.i18n import i18n


class Config(
    commands.Cog,
    name=i18n("cogs.admin.name"),
    description=i18n("cogs.admin.description"),
):
    """Set or get configuration parameters."""

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
        self,
        ctx,
        key: typing.Optional[str],
        *values,
    ):
        """Defines or shows configuration parameters."""

        # Key is none -> getting full configuration
        if key is None:
            configuration = config.to_dict()

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

        # No values but key -> getting config parameter
        elif len(values) == 0:
            value = config.get(key)

            message = i18n(
                "messages.config_item_is", {"key": key, "value": value}
            )

        # Both key and value are set -> set config parameter
        else:
            value = values[0] if len(values) == 1 else list(values)
            config.set(key, value)

            message = i18n(
                "messages.config_item_set_to", {"key": key, "value": value}
            )

        # Send what has been done
        await ctx.send(embed=discord.Embed(description=message))

    @commands.command(brief=i18n("commands.reschedule.brief"))
    async def reschedule(self, ctx):
        """Manually reschedules the job after an interval change."""

        ctx.bot.reschedule_job()
        await ctx.send(
            i18n(
                "messages.rescheduled_to", {"interval": config.get("interval")}
            )
        )

    @commands.command(brief=i18n("commands.trigger.brief"))
    async def trigger(self, ctx):
        """Manually starts sending a subject."""

        await ctx.bot.send_subject()


def setup(bot):
    bot.add_cog(Config(bot))

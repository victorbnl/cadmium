"""Commands for bot administration."""

from discord.ext import commands

from cadmium.i18n import i18n


class Admin(
    commands.Cog,
    name=i18n('cogs.admin.name'),
    description=i18n('cogs.admin.description'),
):
    """Commands for bot administration."""

    @commands.command(brief=i18n('commands.trigger.brief'))
    async def trigger(self, ctx):
        """Manually send a subject."""

        await ctx.bot.send_subject()


def setup(bot):
    bot.add_cog(Admin(bot))

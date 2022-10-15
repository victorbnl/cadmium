"""Commands for testing code."""

from discord.ext import commands


class Test(commands.Cog):
    """Commands for testing code."""

    @commands.group()
    async def test(self, ctx):
        """Test command group."""

    @test.command()
    async def simulate(self, ctx):
        """Simulate a subject sending in the current channel."""

        await ctx.bot.send_subject(channel_id=ctx.channel.id)

    @test.command()
    async def error(self, ctx):
        """Simulate an error."""

        return 1/0


def setup(bot):
    bot.add_cog(Test(bot))

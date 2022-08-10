import discord
from discord.ext import commands

from cadmium.get_subject import get_subject

class Test(commands.Cog):
    @commands.group()
    async def test(self, ctx):
        pass

    @test.command()
    async def simulate(self, ctx):
        image = get_subject()
        await ctx.send(file=discord.File(fp=image, filename="subject.jpg"))

def setup(bot):
    bot.add_cog(Test(bot))

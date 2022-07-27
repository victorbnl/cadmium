#-*- coding: utf-8 -*-

import discord
from discord.ext import commands

class MyHelp(commands.HelpCommand):
    
    async def send_bot_help(self, mapping):
        """Main help menu"""

        channel = self.get_destination()

        embed = discord.Embed(colour=0x2b5966)
        embed.set_footer(text="Pour plus d'informations sur une commande : !help [command]")

        for cog, commands in mapping.items():
            if len(commands) > 0:
                cog_name = getattr(cog, "qualified_name", "Autres")
                value = ""
                for command in commands:
                    value += "⠀- `{command.name}`: {command.brief}\n"
                embed.add_field(name=cog_name, value=value+"\n", inline=False)
        
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        """Command help menu"""
        
        channel = self.get_destination()

        embed = discord.Embed(
            title=command.name.capitalize(),
            description=command.brief,
            colour=0x34484c
        )

        for param in command.params:
            if param == "type":
                print(dir(command.params[param]))
                print(command.params[param].annotation)

        usage = f"{self.context.clean_prefix}{command.name} {' '.join(f'[{arg}]' for arg in command.clean_params)}"
        embed.add_field(
            name="Utilisation",
            value=f"```{usage}```",
            inline=False
        )

        args = []
        for param in command.clean_params.values():
            try:
                desc = command.extras["args"][param.name]
            except KeyError:
                desc = ""
            args.append({
                "name": param.name,
                "desc": desc
            })

        if command.extras:
            embed.add_field(
                name="Paramètres",
                value="\n".join([f"⠀•⠀**{arg['name']}** : {arg['desc']}" for arg in args]),
                inline=False
            )

        embed.add_field(
            name="Alias",
            value=", ".join([f"`{command.name}`"] + [f"`{alias}`" for alias in command.aliases]),
            inline=False
        )

        await channel.send(embed=embed)

    async def send_group_help():
        pass

    async def send_cog_help():
        pass

def setup(bot):
    bot.help_command = MyHelp()

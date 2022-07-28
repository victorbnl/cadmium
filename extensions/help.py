#-*- coding: utf-8 -*-

import discord
from discord.ext import commands

import utils.config as config

class MyHelp(commands.HelpCommand):
    
    async def send_bot_help(self, mapping):
        """Main help menu"""

        channel = self.get_destination()

        fields = []
        for cog, commands in mapping.items():
            if len(commands) > 0:
                cog_name = getattr(cog, "qualified_name", "Autres")
                value = ""
                for command in commands:
                    value += f"⠀- `{command.name}`{('', f': {command.brief}')[bool(command.brief)]}\n"
                fields.append({
                    "name": cog_name,
                    "value": value+"\n",
                    "inline": False
                })

        await channel.send_embed({
            "footer": {"text": "Pour plus d'informations sur une commande : !help [command]"},
            "fields": fields
        })

    async def send_command_help(self, command):
        """Command help menu"""
        
        channel = self.get_destination()

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

        await channel.send_embed({
            "title": command.name.capitalize(),
            "description": command.brief,
            "fields": [
                {
                    "name": "Utilisation",
                    "value": f"```\n{self.context.clean_prefix}{command.name} {' '.join(f'[{arg}]' for arg in command.clean_params)}\n```"
                },
                {
                    "name": "Paramètres",
                    "value": "\n".join([f"⠀•⠀**{arg['name']}** : {arg['desc']}" for arg in args]),
                },
                {
                    "name": "Alias",
                    "value": ", ".join([f"`{command.name}`"] + [f"`{alias}`" for alias in command.aliases]),
                }
            ]
        })

    async def send_group_help():
        pass

    async def send_cog_help():
        pass

def setup(bot):
    bot.help_command = MyHelp()

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import discord
from discord.ext import commands

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from dotenv import load_dotenv
import os

import utils.subject as subject
import utils.config as config

load_dotenv()
def getenv(var):
    return os.environ[f"SUBJECTS_BOT_{var}"]

token = getenv("TOKEN")
guild_id = int(getenv("GUILD"))
role_id = int(getenv("ROLE"))

intents = discord.Intents.default()
intents.message_content = True

class SubjectsBot(commands.Bot):

    async def block_other_guilds_check(self, ctx):
        role = discord.utils.find(lambda r: r.id == role_id, ctx.guild.roles)
        return ctx.guild.id == guild_id and role in ctx.author.roles

    def __init__(self):
        super().__init__(command_prefix='$', intents=intents)

        self.add_check(self.block_other_guilds_check)

        for ext in ("manage_lists", "admin", "help", "error"):
            self.load_extension("extensions.{}".format(ext))
            print("Loaded extension {}".format(ext))

    async def send_subject(self):
        channel_id = int(config.get("channel").replace("<#", "").replace(">", ""))
        message = config.get("message")
        todays_subject = subject.get_subject()

        channel = bot.get_channel(channel_id)

        await channel.send(message.format(todays_subject))

    async def on_ready(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.send_subject, CronTrigger.from_crontab(config.get("frequency")))
        scheduler.start()

        print("Ready!")

bot = SubjectsBot()
bot.run(token)

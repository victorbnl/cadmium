#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import discord
from discord.ext import commands

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from dotenv import load_dotenv
import os

import utils.data as data
import utils.config as config

load_dotenv()
token = os.environ["SUBJECTS_BOT_TOKEN"]
guild = int(os.environ["SUBJECTS_BOT_GUILD"])

intents = discord.Intents.default()
intents.message_content = True

class SubjectsBot(commands.Bot):

    async def block_other_guilds_check(self, ctx):
        return ctx.guild.id == guild

    def __init__(self):
        super().__init__(command_prefix='$', intents=intents)

        self.add_check(self.block_other_guilds_check)

        for cog in ("manage_lists", "admin", "help", "error"):
            self.load_extension("extensions.{}".format(cog))
            print("Loaded extension {}".format(cog))

    async def send_subject(self):
        channel_id = int(config.get("channel").replace("<#", "").replace(">", ""))
        message = config.get("message")
        subject = data.get_subject()

        channel = bot.get_channel(channel_id)

        await channel.send(message.format(subject))

    async def on_ready(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.send_subject, CronTrigger.from_crontab(config.get("frequency")))
        scheduler.start()

        print("Ready!")

bot = SubjectsBot()
bot.run(token)

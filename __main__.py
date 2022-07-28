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
import utils.artwork as artwork
import utils.send_embed

load_dotenv()
def getenv(var):
    return os.environ[f"SUBJECTS_BOT_{var}"]

token = getenv("TOKEN")
guild_id = int(getenv("GUILD"))
role_id = int(getenv("ROLE"))
prefix = getenv("PREFIX")

intents = discord.Intents.default()
intents.message_content = True

class SubjectsBot(commands.Bot):

    async def block_other_guilds_check(self, ctx):
        role = discord.utils.find(lambda r: r.id == role_id, ctx.guild.roles)
        return ctx.guild.id == guild_id and role in ctx.author.roles

    def __init__(self):
        super().__init__(command_prefix=prefix, intents=intents)

        self.add_check(self.block_other_guilds_check)

        for ext in ("manage_lists", "admin", "help", "error"):
            self.load_extension(f"extensions.{ext}")
            print(f"Loaded extension {ext}")

    async def send_subject(self):
        channel_id = int(config.get("channel").replace("<#", "").replace(">", ""))
        message = config.get("message")
        todays_subject = subject.get_subject()

        channel = self.get_channel(channel_id)

        image = artwork.subject_to_artwork(todays_subject)

        await channel.send(file=discord.File(fp=image, filename="subject.jpg"))
    
    def reschedule_job(self):
        self.scheduler.reschedule_job("send_subject", trigger=CronTrigger.from_crontab(config.get("interval")))

    async def on_ready(self):
        self.scheduler = AsyncIOScheduler()
        self.scheduler.add_job(self.send_subject, CronTrigger.from_crontab(config.get("interval")), id="send_subject")
        self.scheduler.start()

        print("Ready!")

bot = SubjectsBot()
bot.run(token)

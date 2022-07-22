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

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

token = os.environ["SUBJECTS_BOT_TOKEN"]
guild = int(os.environ["SUBJECTS_BOT_GUILD"])

async def send_subject():
    channel_id = int(config.get("channel").replace("<#", "").replace(">", ""))
    message = config.get("message")
    subject = data.get_subject()

    channel = bot.get_channel(channel_id)

    await channel.send(message.format(subject))

@bot.check
async def block_other_guilds(ctx):
    return ctx.guild.id == guild

@bot.event
async def on_ready():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_subject, CronTrigger.from_crontab(config.get("frequency")))
    scheduler.start()

    print("Ready!")

@bot.command(brief="Lancer manuellement la génération d'un sujet")
async def trigger(ctx):
    await send_subject()

for cog in ("manage_lists", "config", "help"):
    bot.load_extension("extensions.{}".format(cog))
    print("Loaded extension {}".format(cog))

bot.run(token)

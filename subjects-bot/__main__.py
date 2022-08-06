"""Main file, starts the bot and the scheduler."""

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from utils import env
from utils import config

from bot import SubjectsBot

token = env.get("TOKEN")
guild_id = int(env.get("GUILD"))
role_id = int(env.get("ROLE"))
prefix = env.get("PREFIX")

color = config.get("color")

bot = SubjectsBot(
    guild_id,
    role_id,
    prefix,
    color
)

scheduler = AsyncIOScheduler()
scheduler.add_job(bot.send_subject, CronTrigger.from_crontab(config.get("interval")), id="send_subject")
scheduler.start()

bot.run(token)

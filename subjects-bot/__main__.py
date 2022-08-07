"""Main file, starts the bot and the scheduler."""

from utils import env
from utils import config

from bot import SubjectsBot

token = env.get("TOKEN")
guild_id = int(env.get("GUILD"))
role_id = int(env.get("ROLE"))
prefix = env.get("PREFIX")

color = config.get("color")

bot = SubjectsBot(guild_id, role_id, prefix, color)

bot.run(token)

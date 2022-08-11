"""Main file, starts the bot and the scheduler."""

from cadmium import config
from cadmium.bot import Cadmium
from cadmium.utils import env

# Get environment variables
token = env.get("TOKEN")
guild_id = int(env.get("GUILD"))
role_id = int(env.get("ROLE"))
prefix = env.get("PREFIX")

# Get config
color = int(config.get("color"), 16)

# Define bot
bot = Cadmium(guild_id, role_id, prefix, color)

# Start the bot
bot.run(token)

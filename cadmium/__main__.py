from cadmium.utils import env
from cadmium.bot import CadmiumBot

from loguru import logger


guild_id = env.get('GUILD')
role_id = env.get('ROLE')
token = env.get('TOKEN')

logger.debug(f"Guild ID: {guild_id}")
logger.debug(f"Role ID: {role_id}")

bot = CadmiumBot(
    guild_id=guild_id,
    role_id=role_id,
)

bot.run(token)

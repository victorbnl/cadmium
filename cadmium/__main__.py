from cadmium import env
from cadmium.bot import CadmiumBot

bot = CadmiumBot(
    guild_id=env.get('GUILD'),
    role_id=env.get('ROLE'),
)

bot.run(env.get('TOKEN'))

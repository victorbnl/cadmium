from cadmium.lists import lists
from cadmium import config
from cadmium.i18n import i18n

class Dashboard():

    def __init__(self, bot):

        self.bot = bot
        self.channel_id = int(config.get("dashboard_channel"))
        self.message = None
    
    async def update(self):

        # Content
        content = ("\n\n".join(
            "\n".join(
                (
                    f"**__{i18n(f'lists.{lst}').capitalize()}__**",
                    ", ".join(
                        f"`{word}`"
                        for word in lists[lst].items()
                    )
                )
            )
            for lst in ('nouns', 'verbs', 'adjectives', 'adverbs')
        ))

        # Update message
        if self.message:
            await self.message.edit(content=content)
        else:
            self.message = await self.bot.get_channel(self.channel_id).send(content)
    
    async def on_ready(self):
        await self.bot.get_channel(self.channel_id).purge()
        await self.update()
    
    async def on_message(self, message):
        pass

        parsed = message.content.split()

        if message.content:

            if parsed[0] in ("noun", "nouns", "verb", "verbs", "adjective", "adjectives", "adverb", "adverbs"):

                await message.delete()
            
                list_ = parsed[0]
                plurals = {'noun': 'nouns', 'verb': 'verbs', 'adjective': 'adjectives', 'adverb': 'adverbs'}
                if list_ in plurals.keys():
                    list_ = plurals[list_]
                list_ = lists[list_]

                words = parsed[1:]

                with lists["db"].atomic():
                    for word in words:
                        list_.update(word)
                
                await self.update()

def setup(bot):

    dashboard = Dashboard(bot)

    bot.add_listener(dashboard.on_ready)
    bot.add_listener(dashboard.on_message)

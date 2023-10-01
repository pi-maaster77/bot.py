from config import consola,  general
import random

def exportacion(bot):
    @bot.event
    async def roles():
        if message.channel == consola:
            if "[LP] Searching" in message.content.lower():
                await message.channel.send("algo")
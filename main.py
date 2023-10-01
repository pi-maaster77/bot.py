# este es el archivo principal del bot
# contiene todo el codigo necesario para que el bot arranque
import discord, \
    config, \
    listador                                              # se importan las librerias necesarias  
from discord.ext import commands
exec(listador.cargarEventos())                            # se ejecuta el string
intents = discord.Intents.default()                       # se define lo que el bot puede o no hacer
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix="!")   # se define lo basico del bot
eventos(bot)                                # se importan los eventos del bot
bot.run(config.token)                                     # se inicia secion 
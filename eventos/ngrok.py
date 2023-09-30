#codigo para dar la ip del server que usa la aplicacion ngrok

from pyngrok import ngrok                                              # importa la libreria del programa
from config import botchat, general
def exportacion(bot):                                                  # exporta el evento
    @bot.event
    async def on_message(message):
        if message.channel.id == botchat:
            if "ngrok" in message.content.lower():                                 # verifica si el mensaje dice "ngrok"
                tunnel = ngrok.connect(addr="5000", proto="tcp")           # define las caracteristicas de la conexion 
                ip = tunnel.public_url                                     # (en este caso se comparte el puerto 5000 con protocolo tcp)
                
                objetivo = bot.get_channel(general)

                if objetivo:
                    await objetivo.send(f"ip: {ip}")
        await bot.process_commands(message)
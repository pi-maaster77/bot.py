# evento de testeo

def exportacion(bot):                                  # se exporta el codigo
    @bot.event                                         # se importan los modulos necesarios 
    async def on_message(message):                     # se define el evento
        if message.content == "hola":                  # verifica que un mensaje contenga la palabra clave "hola"
            await message.channel.send("holi")         # responde
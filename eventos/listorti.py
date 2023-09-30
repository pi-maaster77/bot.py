# evento de cuando el bot se inicia

def exportacion(bot):     # exporta el evento
    @bot.event            # importa los modulos necesarios
    async def on_ready(): # define el evento 
        print("listorti") # dice por consola que el bot esta listo para todo

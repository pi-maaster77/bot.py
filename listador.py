import os                                                               # libreria necesaria para listar los archivos y generar el archivo final  

def cargarEventos():                                                    # se encarga de hacer que el resto del codigo sea ejecutable por el archivo principal

    dir = "./eventos"                                                   # define el directorio donde se buscaran los archivos

    if os.path.exists(dir):                                             # se asegura que el directorio exista                                          
        archivos = [                                                    
            archivo for archivo in os.listdir(dir)                      # se crea una lista de los archivos que contiene el directorio
            if archivo != "__pycache__"                                 # excluyendo al directorio de cache que se genera automaticamente 
        ]
        librerias = ""
        for libreria in archivos:
            librerias += f"    {libreria[:-3]}.exportacion(bot) \n"
        
        crudo = str(archivos)\
        .replace("[", "")\
        .replace("'", "")\
        .replace("]", "")\
        .replace(".py", "")\
        .replace(",", ", \\\n   ")                                      # genera una oracion en crudo
        return \
            f"""from eventos import {crudo}
            
def eventos(bot):                                                       
{librerias}"""                                                          # devuelve un parrafo con todas las librerias

# Este archivo se encarga de listar los eventos de la carpeta con dicho nombre 
# Ademas de facilitar un formato para que se puedan importar  
# todos estos se almacenaran en el archivo de salida que en este caso se llama "lista_eventos.py"

import os                                                               # libreria necesaria para listar los archivos y generar el archivo final  

def cargarEventos():                                                    # se encarga de hacer que el resto del codigo sea ejecutable por el archivo principal

    dir = "./eventos"                                                   # define el directorio donde se buscaran los archivos

    if os.path.exists(dir):                                             # se asegura que el directorio exista
        salida = "lista_eventos.py"                                     # nombra el archivo de salida
        
        archivos = [                                                    
            archivo for archivo in os.listdir(dir)                      # se crea una lista de los archivos que contiene el directorio
            if archivo != "__pycache__"                                 # excluyendo al directorio de cache que se genera automaticamente 
        ]
        crudo = str(archivos)\
        .replace("[", "")\
        .replace("'", "")\
        .replace("]", "")\
        .replace(".py", "")\
        .replace(",", ", \\\n   ")                                      # genera una oracion en crudo
        with open(salida, 'w') as archivo:                              # crea el archivo
            archivo.write("from eventos import ")
            archivo.write(crudo) 

            archivo.write("\n\ndef eventos(bot):\n")                    # crea la funcion ejecutable 
            for nom in archivos:                                        # llama a todas las funciones de eventos
                nombre = os.path.splitext(nom)[0]                       
                archivo.write(f"    {nombre}.exportacion(bot) \n")
cargarEventos()
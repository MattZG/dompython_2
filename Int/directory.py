import os

def crear_directorio(ruta):
    try:
        os.mkdir(ruta)
    except OSError as e:
        print(e)

crear_directorio("directorio_vacio")

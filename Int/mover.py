import shutil

def mover_archivo(ubicacion_actual, ubicacion_nueva):
    try:
        shutil.move(ubicacion_actual, ubicacion_nueva)
    except Exception as e:
        print(e)

mover_archivo("archivo_ejemplo/archivo.txt","archivo.txt")

#ERROR
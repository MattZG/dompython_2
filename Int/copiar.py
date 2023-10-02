import shutil

def copiar(ubicacion_actual, ubicacion_nueva):
    try:
        shutil.copy(ubicacion_actual, ubicacion_nueva)
    except Exception as e:
        print(e)


copiar('archivos_ejemplo/archivo.txt', "archivo.txt")
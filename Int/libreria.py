import importlib

def importar_modulo(ruta_modulo):
    try:
        modulo = importlib.import_module(ruta_modulo)
        print(f" El modulo {ruta_modulo} si existe.")
    except ModuleNotFoundError:
        print(f"No se encontro {ruta_modulo}")

def invocar_funcion(ruta_modulo, nombre_funcion):
    modulo = importar_modulo(ruta_modulo)
    if nombre_funcion not in modulo:
        print("La funcion no existe en el modulo")
        return
    funcion = getattr(modulo, nombre_funcion)
    if not hasattr(funcion, "__call__"):
        print("No es posible invocar la funcion")
        return
    
    funcion(*args, **kwargs)



ruta_modulo = 'archivos_ejemplo.ejemplo'
nombre_funcion = 'funcion_ejemplo'
invocar_funcion(ruta_modulo, nombre_funcion)

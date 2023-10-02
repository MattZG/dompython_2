import time

def crear_diccionario():
    inicio = time.time()
    diccionario = {
        'Nombre': 'Ana',
        'Apellido': 'Pinto',
    }
    time.sleep(2)
    print("Tiempo (s):", time.time() - inicio)
    return diccionario

crear_diccionario()

#forma poco optima

def contar_tiempo(funcion):
    def medir_duracion(*args, **kwargs):
        inicio = time.time()
        funcion(*args,**kwargs)
        print("Tiempo (s):" , time.time() - inicio)
    return medir_duracion

@contar_tiempo
def crear_diccionario():
    diccionario = {
        'Nombre': 'Ana',
        'Apellido': 'Pinto',
    }
    return diccionario

crear_diccionario()

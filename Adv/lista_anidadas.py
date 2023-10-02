lista_anidada = [
    [1,2,3],
   ["a", "b", "c"],
    ["d", "e", "f"]
]

def recorrer_lista(lista):
    for elemento in lista:
        if type(elemento) is list:
            for item in elemento:
                print(item)
        else:
            print(elemento)

recorrer_lista(lista_anidada)

lista = [[1,2,3],4,5,6]

recorrer_lista(lista)
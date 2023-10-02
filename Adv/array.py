import numpy as np

lista = [1,2,3]
lista_anidada = [[1,2,3],[4,5,6]]

array = np.array(lista)
print(array, type(array))

matrix = np.array(lista_anidada)
print(matrix, type(matrix))

matrix_1 = np.matrix(lista_anidada)
print(matrix_1, type(matrix_1))

matrix_2 = np.zeros((2,2))
print(matrix_2)
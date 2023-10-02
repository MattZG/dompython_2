import numpy as np

matrix_a = np.array([[1,2],[3,4]])
matrix_b = np.array([[1,2],[3,4]])

sum = np.add(matrix_a,matrix_b)
print(sum)

sub = np.subtract(matrix_b, matrix_a)
print(sub)

dot = np.dot(matrix_a, matrix_b)
print(dot)
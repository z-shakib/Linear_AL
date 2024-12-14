import numpy as np
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

#! Matrices:
A = np.array([
    [1,2],
    [3,4]
])
B = np.array([
    [5,6],
    [7,8]
])

#Addition:
addition = A + B
print(f'Matrix Addition:\n {addition}')

#!Subtraction
subtraction = A - B
print("Matrix Subtraction:\n", subtraction)

#! Multiplication: if 1st matrix columns = 2nd matrix rows
# Matrix Multiplication
C = np.array([[1, 2], [3, 4]])
D = np.array([[5, 6], [7, 8]])

multiplication = np.dot(C, D)  # Dot product
print("Matrix Multiplication:\n", multiplication)


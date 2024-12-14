import numpy as np
from numpy.ma.core import identity

#! Inverse of matrix
F = np.array([[1,2], [3,4]])
inverse = np.linalg.inv(F)
print(f'Inverse of matrix: \n {inverse}')

#! Determinant of a matrix
determinant = np.linalg.det(F)
print(f'Determinant of matrix: \n {determinant}')

#! Identity matrix:
identityMatrix = np.eye(3, dtype='int') #3*3 matrix
print(f'Identity Matrix: \n {identityMatrix}')

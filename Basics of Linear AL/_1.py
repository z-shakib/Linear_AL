import numpy as np 
#! Scalar: 
scalar = 5 
print(f'Scalar: {scalar}')

#! Vector: 
vector = np.array([1,2,3])
print(f'vector: {vector}')

#! Matrix:
matrix = np.array([[1,2], [3,4]])
print(f'Matrix\n: {matrix}')

#! Tensor:
tensor = np.array([[
    [1,2],
    [3,4],
    [5,6],
    [7,8]
]])
print(f'Tensor\n: {tensor}')

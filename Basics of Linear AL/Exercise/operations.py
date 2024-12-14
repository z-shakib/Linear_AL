import numpy as np
#! Matrix operation:
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

#! Matrix addition:
mat_addition = A + B
print(f'Addition of matrix A and B is: \n {mat_addition}')

#! Matrix Subtraction
mat_subtraction = A - B
print(f'Subtraction of matrix A and B is: \n {mat_subtraction}')

#! Matrix Multiplication:
mat_multiplication = A * B
print(f'Multiplication of matrix A and B is: \n {mat_multiplication}')


C = np.array([[2,4],
              [6,8]])
print(f'Transpose of matrix C is: \n {C.T}')

#! Determinant and Inverse
D = np.array([[2,3], [1,4]])
det = np.linalg.det(D)
print(f'Determinant of D is: \n {det}')
if det != 0:
    print(f'The inverse of matrix D is: \n {np.linalg.inv(D)}')


#! Identity matrix :
print(f'The 4*4 identity matrix is: \n {np.eye(4, dtype='int')}')

#! Tensor:
tensor = np.random.randint(1,11, size=(2,2,2))
print(f'Tensor: \n {tensor}')
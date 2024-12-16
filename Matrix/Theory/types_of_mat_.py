import numpy as np

# Diagonal matrix create
D = np.diag([5, 3, 7])
print("Diagonal Matrix:")
print(D)

# Symmetric matrix create: A[i][j] == A[j][i]
S = np.array([[1, 2, 3],
              [2, 4, 5],
              [3, 5, 6]])
print("Symmetric Matrix:")
print(S)
#! check if is symmetric:
is_symmetric = np.array_equal(S, S.T) #Transpose check
print('Is the matrix symmetric?', is_symmetric)

#! Identity matrix create
I = np.eye(3, dtype=int)  # 3x3 Identity matrix
print("Identity Matrix:")
print(I)

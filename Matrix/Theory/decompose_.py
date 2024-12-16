import numpy as np
from scipy.linalg import lu, qr

#! Example matrix
A = np.array([[4,3], [6,3]])

# LU decomposition
P, L, U = lu(A)  # P: Permutation, L: Lower, U: Upper
print("Original Matrix (A):")
print(A)

print("\nPermutation Matrix (P):")
print(P)

print("\nLower Triangular Matrix (L):")
print(L)

print("\nUpper Triangular Matrix (U):")
print(U)

# Verify A = P * L * U
A_reconstructed = P @ L @ U
print("\nReconstructed Matrix (P * L * U):")
print(A_reconstructed)


#! QR Decomposition:
B = np.array([[12, -51, 4],
              [6, 167, -68],
              [-4, 24, -41]])
#! Decompose:
Q, R = qr(B)
print("Original Matrix (A):")
print(B)

print("\nOrthogonal Matrix (Q):")
print(Q)

print("\nUpper Triangular Matrix (R):")
print(R)

# Verify B = Q * R
B_reconstructed = Q @ R
print("\nReconstructed Matrix (Q * R):")
print(B_reconstructed)

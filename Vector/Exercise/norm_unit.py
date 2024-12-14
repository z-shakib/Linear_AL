import numpy as np
#! Norm of a vector: find the norm of the vector
v = np.array([3,4])
print(f'Vector Norm (Magnitude): {np.linalg.norm(v)}')

#! Confirming the magnitude of the unit vector is 1.
vector = np.array([7, 24])
unit_of = vector / np.linalg.norm(vector)
print(unit_of)
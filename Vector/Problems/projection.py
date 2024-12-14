import numpy as np
#! Vectors:
v1 = np.array([2,4,6])
v2 = np.array([1,1,1])

projection = (np.dot(v1, v2) / np.linalg.norm(v2)**2) *v2
print(f'Projection of {v1} and {v2}: {projection}')


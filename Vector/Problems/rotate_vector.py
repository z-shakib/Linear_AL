import numpy as np

# Vector define
v = np.array([2, 3])

# 90° rotate er jonno rotation matrix
rotation_matrix = np.array([[0, -1], [1, 0]])

# Rotation apply kora
rotated_vector = np.dot(rotation_matrix, v)
print(f'The 90° rotated vector is: {rotated_vector}')

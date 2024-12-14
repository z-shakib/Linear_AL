import numpy as np
#! Vectors:
v1 = np.array([1,2])
v2 = np.array([3,4])

#! Angles Between Vectors:
cos_theta = np.degrees((np.dot(v1, v2)) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
print(cos_theta)

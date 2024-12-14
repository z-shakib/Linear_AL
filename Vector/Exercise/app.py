import numpy as np
#! Find angles between Vectors
v1 = np.array([2,4,6])
v2 = np.array([1,1,1])

cos_theta = np.degrees((np.dot(v1, v2)) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
print(cos_theta)
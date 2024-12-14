import numpy as np
#! Check orthogonality:
v1 = np.array([1,2,3])
v2 = np.array([-3, -6, -9])

#! Checking..
check = 'Orthogonal' if np.dot(v1, v2) == 0 else 'Not Orthogonal'
print(check)

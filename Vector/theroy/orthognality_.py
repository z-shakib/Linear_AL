#! Orthogonality (Perpndicular vectors)
import numpy as np
#! if two vector is orthogonal than the product of them is 0
v3 = np.array([1,0])

v4 = np.array([0,1])
#! Do not product should be 0
if np.dot(v3, v4) == 0:
    print('Vector are orthogonal')
else:
    print('Vector are not orthogonal')


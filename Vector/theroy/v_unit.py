import numpy as np
#! unit vector is a vector which value is 1
v1 = np.array([1,2,3])
v_unit = v1 / np.linalg.norm(v1)
print(f'Unit Vector: {v_unit}')

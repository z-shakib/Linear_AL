import numpy as np
v = np.array([2,3])
rotate = np.rot90(v, k = 1, axes= (0,1))
print(f'The 90degree rotated array is: {rotate}')

import numpy as np
#! Vectors:
v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

#! Weight:
w1 = 0.3
w2 = 0.7

weighted_avg = (w1 * v1) + (w2 * v2)
print(f'The weighted average of v1: {v1} and v2: {v2} is: {weighted_avg}')
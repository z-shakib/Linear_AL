import numpy as np
#! Vectors:
v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

#! Weight:
w1 = 0.3
w2 = 0.7

weighted_avg = w2 * v1 + w2 * v2
print(f'The weighted avg is is: {weighted_avg}')

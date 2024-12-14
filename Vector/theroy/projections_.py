import numpy as np
v1 = np.array([1,2,3])
v2 = np.array(([4,5,6]))

#! Projections od v1 on to v2
proj_v1_on_v2 = (np.dot(v1,v2) / np.linalg.norm(v2)**2) * v2
print(f'Projection of v1 onto v2: {proj_v1_on_v2}')

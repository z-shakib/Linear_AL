import numpy as np
def check_orthogonal(v1, v2):
    if np.dot(v1, v2) == 0:
        print(f'Vectors {v1} and {v2} are Orthogonal')
    else:
        print(f'Vectors {v1} and {v2} are not Orthogonal')
    return

v1 = np.array([1, -1, 0])
v2 = np.array([1,1,0])
check_orthogonal(v1, v2)
#!===============
ve3 = [2,3]
ve4 = [-3,1]
check_orthogonal(ve3, ve4)

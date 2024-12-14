import numpy as np
#! Dot product collection:
v1 = [1,2,3]
v2 = [4,1,1]
if np.dot(v1, v2) >= 10:
    print(f'The dot product of {v1} and {v2} is greater than 10')
else:
    print(f'The dot product of {v1} and {v2} is not greater than 10')

#! Cross Product:
v1 = [1,0,0]
v2 = [0,1,0]

print(f'the cross product of {v1} and {v2} is: \n {np.cross(v1, v2)}')


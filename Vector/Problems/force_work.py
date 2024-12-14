import numpy as np
Force = np.array([10, 20, 15])
Direction = np.array([2,3,1])

work_done = np.dot(Force, Direction)
print(f'The force is {Force} and Direction is {Direction} so work done is: \n {work_done}W')



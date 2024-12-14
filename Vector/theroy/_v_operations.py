#! Vector addition and substraction:
import numpy as np

v1 = np.array([1,2,3])
v2 = np.array(([4,5,6]))

#! Addition:
v_Add = v1 + v2
print(f'Vector Addition: {v_Add}')

#! Subtraction:
v_sub = v1 - v2
print(f'Vector Subtraction: {v_sub}')

#! scalar multiplication:
scalar= 3
v_scaled = scalar * v1
print(f'Scalar Multiplication: {v_scaled}')

# Dot product
v_dot = np.dot(v1, v2)
print(f"Dot Product: {v_dot}")

# Cross product
v_cross = np.cross(v1, v2)
print(f"Cross Product: {v_cross}")

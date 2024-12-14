import numpy as np

matrix = np.array([[1, 2], [3, 4]])

# Total sum of all elements
total = np.sum(matrix)
print(f"Sum of all elements: {total}")

# Row-wise sum
row_sum = np.sum(matrix, axis=1)
print(f"Row-wise sum: {row_sum}")

# Column-wise sum
column_sum = np.sum(matrix, axis=0)
print(f"Column-wise sum: {column_sum}")

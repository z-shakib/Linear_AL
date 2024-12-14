import numpy as np

# Sales data for two weeks
P1 = np.array(
    [100, 200])

P2 = np.array(
    [150, 250])

# Total sales sum for two weeks
total_sales = np.sum(P1) + np.sum(P2)
print(f"The total sales for both weeks is: {total_sales}")

#! check contribution:
if np.linalg.norm(P1) > np.linalg.norm(P2):
    print(f'{P1} Product more contribution than {P2}')
else:
    print(f'{P1} Product less contribution than {P2}')

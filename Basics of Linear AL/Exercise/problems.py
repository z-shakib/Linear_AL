import numpy as np

# Sales data for two weeks
week_1 = np.array([
    [100, 200],
    [150, 250]
])

week_2 = np.array([
    [110, 190],
    [160, 240]
])

# Total sales sum for two weeks
total_sales = np.sum(week_1) + np.sum(week_2)
print(f"The total sales for both weeks is: {total_sales}")

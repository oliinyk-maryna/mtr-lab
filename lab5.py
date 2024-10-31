import numpy as np

data = np.array([
    [15, 10, 8, 7],   # Rye
    [19, 13, 10, 6],  # Oats
    [20, 15, 10, 8],  # Wheat
    [21, 18, 10, 7]   # Buckwheat
])

p = np.array([0.1, 0.5, 0.3, 0.1])

cultures = ["Rye", "Oats", "Wheat", "Buckwheat"]

average_profits = np.dot(data, p)

variances = np.sum(p * (data - average_profits[:, None])**2, axis=1)

coefficients_of_variation = np.sqrt(variances) / average_profits

print("Average profit for each crop:")
for crop, avg in zip(cultures, average_profits):
    print(f"{crop}: {avg:.2f}")

print("\nVariance for each crop:")
for crop, var in zip(cultures, variances):
    print(f"{crop}: {var:.2f}")

print("\nCoefficient of variation for each crop:")
for crop, cv in zip(cultures, coefficients_of_variation):
    print(f"{crop}: {cv:.4f}")

optimal_avg = np.argmax(average_profits)
optimal_var = np.argmin(variances)
optimal_cv = np.argmin(coefficients_of_variation)

print("\nOptimal choice based on maximum average profit:", cultures[optimal_avg])
print("Optimal choice based on minimum variance:", cultures[optimal_var])
print("Optimal choice based on minimum coefficient of variation:", cultures[optimal_cv])


import numpy as np

F = np.array([
    [200, 300, 150],
    [750, 200, 350],
    [250, 800, 350],
    [800, 500, 450]
])

P = np.array([0.1, 0.5, 0.4])
V = np.array([2, 1])

expected_profits = np.dot(F, P)
variances = np.var(F, axis=1)
weighted_decision_scores = -V[0] * expected_profits + V[1] * variances
best_decision_index = np.argmin(weighted_decision_scores)

print("Expected Profits:", np.round(expected_profits, 2))
print("Variances:", np.round(variances, 2))
print("Weighted Decision Scores:", np.round(weighted_decision_scores, 2))
print("Best Decision Index (0-based):", best_decision_index)
print("Best Decision Expected Profit and Variance:", round(expected_profits[best_decision_index], 2), round(variances[best_decision_index], 2))

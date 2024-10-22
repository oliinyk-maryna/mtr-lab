''' 3. Акції виду А1, А2, А3 мають, відповідно, сподівані норми прибутку
20%, 40% та 60%, середньоквадратичні відхилення 10%, 18% та 30%, коефіцієнти 
кореляції p12 = 1, p13 = – 1 та p23 = – 1. Необхідно:
а) визначити структуру ПЦП, що має найбільшу сподівану норму прибутку при 
мінімальному ризику;
б) побудувати множини допустимих та ефективних ПЦП.
'''

import numpy as np
import matplotlib.pyplot as plt

# Дані для активів
returns = np.array([0.20, 0.40, 0.60])  # очікувані норми прибутку для A1, A2, A3
std_devs = np.array([0.10, 0.18, 0.30])  # стандартні відхилення для A1, A2, A3

corr_matrix = np.array([
    [1, 1, -1],
    [1, 1, -1],
    [-1, -1, 1]
])

# коваріаційна матриця
cov_matrix = np.outer(std_devs, std_devs) * corr_matrix


# обчислення оптимального портфеля
def optimal_portfolio(returns, cov_matrix):
    cov_matrix += np.eye(cov_matrix.shape[0]) * 1e-8 

    inverse_cov = np.linalg.inv(cov_matrix)
    ones = np.ones(len(returns))

    numerator = np.dot(inverse_cov, returns)
    denominator = np.dot(ones, np.dot(inverse_cov, returns))
    weights = numerator / denominator

    port_return = np.dot(weights, returns)
    port_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    return weights, port_return, port_risk

def generate_portfolios(num_portfolios, returns, cov_matrix):
    np.random.seed(42)
    portfolio_returns = []
    portfolio_risks = []
    portfolio_weights = []
    
    for _ in range(num_portfolios):
        weights = np.random.random(len(returns))
        weights /= np.sum(weights)

        port_return = np.dot(weights, returns)
        port_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        
        portfolio_returns.append(port_return)
        portfolio_risks.append(port_risk)
        portfolio_weights.append(weights)
    
    return np.array(portfolio_returns), np.array(portfolio_risks), np.array(portfolio_weights)

# побудова множин допустимих та ефективних ПЦП
def plot_efficient_frontier(returns, risks):
    plt.figure(figsize=(10, 6))
    plt.scatter(risks, returns, c=returns / risks, marker='o')
    plt.title('Feasible and Efficient Portfolios')
    plt.xlabel('Risk (Standard Deviation)')
    plt.ylabel('Return')
    plt.colorbar(label='Sharpe Ratio (Return/Risk)')
    plt.show()

num_portfolios = 5000
portfolio_returns, portfolio_risks, portfolio_weights = generate_portfolios(num_portfolios, returns, cov_matrix)

plot_efficient_frontier(portfolio_returns, portfolio_risks)

# портфель з макс прибутком при мін ризику
sharpe_ratios = portfolio_returns / portfolio_risks
max_sharpe_idx = np.argmax(sharpe_ratios)

optimal_weights, optimal_return, optimal_risk = optimal_portfolio(returns, cov_matrix)

print(f"Optimal portfolio weights: {optimal_weights}")
print(f"Expected return: {optimal_return:.2f}")
print(f"Risk (Standard Deviation): {optimal_risk:.2f}")
print(f"Sharpe Ratio: {sharpe_ratios[max_sharpe_idx]:.2f}")

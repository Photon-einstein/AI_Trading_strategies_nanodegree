import numpy as np
from scipy.stats import norm

mu = -0.2
sigma = 0.15
alpha = 0.99

VaR = sigma * norm.ppf(alpha) + mu
print(f"Value at Risk = {VaR:.3f}")

import numpy as np
from scipy.stats import norm


def black_scholes_call(S0, K, T, r, sigma):
    """
    Black-Scholes price of a European call option.

    S0    : current stock price
    K     : strike price
    T     : time to maturity, in years
    r     : risk-free interest rate, annualized
    sigma : volatility, annualized
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    C0 = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return C0


# Example usage:
# C0 = black_scholes_call(S0=100, K=105, T=0.5, r=0.03, sigma=0.22)

S0 = 5
K = 6
T = 2
r = 0.05
sigma = 0.25

C0 = black_scholes_call(S0, K, T, r, sigma)

d1 = -0.056
d2 = -0.4096

print(f"Phi({d1}) = {norm.cdf(d1)}")
print(f"Phi({d2}) = {norm.cdf(d2)}")
print(f"Call option C0 = ${C0}")

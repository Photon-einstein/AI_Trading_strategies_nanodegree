import numpy as np
from scipy.stats import norm


def expected_shortfall(mu, sigma, confidence):
    ES = mu + sigma / (1 - confidence) * norm.pdf(norm.ppf(confidence))
    return ES


mu = -0.2
sigma = 0.15
confidence = 0.99

shortfall = expected_shortfall(mu, sigma, confidence)
print(f"Expected shortfall = {shortfall:.3f}")

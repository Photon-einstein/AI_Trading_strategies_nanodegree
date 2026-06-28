import json
import numpy as np
from scipy.stats import norm


class GBM:
    def __init__(self):
        self.mu = np.nan
        self.sigma = np.nan

    def forecast(self, S0, t, confidence):
        predicted = S0 * np.exp(self.mu * t)
        mu = (self.mu - self.sigma**2 / 2) * t
        sigma = self.sigma * np.sqrt(t)
        log_return_low, log_return_high = norm.ppf(
            [(1 - confidence) / 2, (1 + confidence) / 2], loc=mu, scale=sigma
        )
        price_low = S0 * np.exp(log_return_low)
        price_high = S0 * np.exp(log_return_high)
        return {
            "confidence": confidence,
            "expected": predicted,
            "interval": [price_low, price_high],
        }


model = GBM()
model.mu = 0.25
model.sigma = 0.1
print(json.dumps(model.forecast(100, 0.5, 0.9)))

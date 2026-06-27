import numpy as np
from scipy.stats import norm

S0 = 5
mu = 0.3
sigma = 0.25
t = 1 / 12

drift = (mu - 0.5 * sigma**2) * t
std = sigma * np.sqrt(t)

print(f"drift (mean of log-return) = {drift:.6f}")
print(f"std dev of log-return      = {std:.6f}")

# 50% CI -> 25th and 75th percentiles
z_75 = norm.ppf(0.75)  # = -norm.ppf(0.25)
print(f"\nz for 75th percentile: {z_75:.6f}")

log_lower = drift - z_75 * std
log_upper = drift + z_75 * std

print(f"\nLog-return interval: [{log_lower:.6f}, {log_upper:.6f}]")

# exponentiate and scale by S0
S_lower = S0 * np.exp(log_lower)
S_upper = S0 * np.exp(log_upper)

print(f"\n50% confidence interval for S_t: [{S_lower:.4f}, {S_upper:.4f}]")

# sanity check via direct percentile of lognormal
# S_t = S0 * exp(drift + std*Z)
direct_lower = S0 * np.exp(drift + std * norm.ppf(0.25))
direct_upper = S0 * np.exp(drift + std * norm.ppf(0.75))
print(f"Sanity check (direct percentiles): [{direct_lower:.4f}, {direct_upper:.4f}]")

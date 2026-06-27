import numpy as np
import pandas as pd
import yfinance as yf
from scipy import stats
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import het_arch

# ---------------------------------------------------------------
# 1. Download data
# ---------------------------------------------------------------
data = yf.download("AAPL", start="2024-01-01", end="2025-01-01")
prices = data["Close"].dropna().squeeze()  # <-- added .squeeze()

# ---------------------------------------------------------------
# 2. Compute log-returns
#    GBM assumes log-returns are i.i.d. Normal(mu_dt, sigma_dt^2)
# ---------------------------------------------------------------
log_returns = np.log(prices / prices.shift(1)).dropna()
log_returns = log_returns.squeeze()  # ensure 1-D Series

n = len(log_returns)
dt = 1 / 252  # one trading day, annualized

# ---------------------------------------------------------------
# 3. Test GBM's assumptions
# ---------------------------------------------------------------
print("=" * 60)
print("TESTING GBM ASSUMPTIONS ON LOG-RETURNS")
print("=" * 60)

# (a) Normality: Shapiro-Wilk + Jarque-Bera
shapiro_stat, shapiro_p = stats.shapiro(log_returns)
jb_stat, jb_p = stats.jarque_bera(log_returns)
skew = stats.skew(log_returns)
kurt = stats.kurtosis(log_returns)  # excess kurtosis (Normal = 0)

print(f"\n[Normality]")
print(f"  Shapiro-Wilk:  stat={shapiro_stat:.4f}, p-value={shapiro_p:.4g}")
print(f"  Jarque-Bera:   stat={jb_stat:.4f}, p-value={jb_p:.4g}")
print(f"  Skewness:      {skew:.4f}  (Normal = 0)")
print(f"  Excess kurtosis: {kurt:.4f}  (Normal = 0; >0 = fat tails)")
if jb_p < 0.05:
    print("  -> Reject normality at 5% level (fat tails / skew likely present)")
else:
    print("  -> Cannot reject normality at 5% level")

# (b) Constant volatility: split sample in half, compare variances
half = n // 2
first_half, second_half = log_returns.iloc[:half], log_returns.iloc[half:]
levene_stat, levene_p = stats.levene(first_half, second_half)

print(f"\n[Constant volatility]")
print(f"  Std dev, first half:  {first_half.std():.5f}")
print(f"  Std dev, second half: {second_half.std():.5f}")
print(f"  Levene's test p-value: {levene_p:.4g}")
if levene_p < 0.05:
    print("  -> Reject equal variance: volatility is NOT constant over the period")
else:
    print("  -> Cannot reject equal variance")

# (c) Autocorrelation in squared returns (volatility clustering / ARCH effect)
sq_returns = log_returns**2
autocorr_lag1 = sq_returns.autocorr(lag=1)
print(f"\n[Volatility clustering]")
print(f"  Autocorrelation of squared returns (lag 1): {autocorr_lag1:.4f}")
print(
    "  (A value clearly away from 0 suggests volatility clustering, "
    "violating the constant-sigma GBM assumption)"
)

# (d) ARCH-LM test: joint test across multiple lags for ARCH effects
#     H0: no ARCH effect (residual variance does not depend on past squared
#     residuals) -- i.e. consistent with GBM's constant-sigma assumption.
arch_lags = 5
lm_stat, lm_p, f_stat, f_p = het_arch(log_returns, nlags=arch_lags)
print(f"\n[ARCH-LM test ({arch_lags} lags)]")
print(f"  LM stat: {lm_stat:.4f}, LM p-value: {lm_p:.4g}")
print(f"  F stat:  {f_stat:.4f},  F p-value:  {f_p:.4g}")
if lm_p < 0.05:
    print(
        "  -> Reject H0: significant ARCH effect (volatility clustering "
        "present across multiple lags, jointly)"
    )
else:
    print("  -> Cannot reject H0: no significant joint ARCH effect detected")

print("\n" + "=" * 60)
print("CONCLUSION: Check the printed diagnostics above. In practice, ")
print("equity returns usually show fat tails and volatility clustering,")
print("so GBM is a simplification, not a great fit. We calibrate it ")
print("anyway below, since it's still a useful baseline model.")
print("=" * 60)

# ---------------------------------------------------------------
# 4. Calibrate GBM via MLE
#    Under GBM: log_return ~ Normal((mu - 0.5*sigma^2)*dt, sigma^2*dt)
# ---------------------------------------------------------------
mean_log_ret = log_returns.mean()
std_log_ret = log_returns.std(ddof=1)

sigma_hat = std_log_ret / np.sqrt(dt)  # annualized volatility
mu_hat = mean_log_ret / dt + 0.5 * sigma_hat**2  # annualized drift

print(f"\nCALIBRATED GBM PARAMETERS (annualized)")
print(f"  mu (drift):      {mu_hat:.4f}  ({mu_hat*100:.2f}% per year)")
print(f"  sigma (vol):     {sigma_hat:.4f}  ({sigma_hat*100:.2f}% per year)")
print(f"  S0 (last price): {prices.iloc[-1]:.2f}")

# ---------------------------------------------------------------
# 5. Sanity check: simulate paths with calibrated params and compare
# ---------------------------------------------------------------
np.random.seed(0)
n_sims = 1000
S0 = prices.iloc[0]
sim_paths = np.zeros((n_sims, n + 1))
sim_paths[:, 0] = S0
for t in range(1, n + 1):
    z = np.random.standard_normal(n_sims)
    sim_paths[:, t] = sim_paths[:, t - 1] * np.exp(
        (mu_hat - 0.5 * sigma_hat**2) * dt + sigma_hat * np.sqrt(dt) * z
    )

plt.figure(figsize=(10, 6))
plt.plot(prices.values, color="black", linewidth=2, label="Actual AAPL price")
plt.plot(sim_paths[:20].T, color="steelblue", alpha=0.3)
plt.title("Actual AAPL 2024 Price vs Simulated GBM Paths (calibrated params)")
plt.xlabel("Trading day")
plt.ylabel("Price ($)")
plt.legend()
plt.tight_layout()
plt.savefig("gbm_vs_actual.png", dpi=120)
print("\nSaved comparison plot to gbm_vs_actual.png")

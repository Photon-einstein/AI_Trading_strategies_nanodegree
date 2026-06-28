import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


class GBM:
    def __init__(self, mu=np.nan, sigma=np.nan):
        self.mu = mu
        self.sigma = sigma

    def simulate(self, N, K, Dt, S0):
        A = np.full(shape=(N + 1, K), fill_value=np.nan)
        A[0, :] = S0
        drift = (self.mu - self.sigma**2 / 2) * np.linspace(Dt, N * Dt, N)
        for i in range(K):
            W = np.cumsum(norm.rvs(scale=np.sqrt(Dt), size=N))
            A[1:, i] = S0 * np.exp(drift + self.sigma * W)
        return A


def running_drawdown(prices):
    """Returns the running drawdown (as a negative fraction) at each point in time."""
    running_max = np.maximum.accumulate(prices)
    drawdown = (prices - running_max) / running_max
    return drawdown


model = GBM(0.4, 0.5)
Dt = 1 / 252
N = 200
K = 5
S0 = 10

A = model.simulate(N, K, Dt, S0)
X = np.linspace(0, N * Dt, N + 1)

fig, axes = plt.subplots(K + 1, 1, figsize=(10, 2.5 * (K + 1)), sharex=True)

# Top plot: all price trajectories together
ax_price = axes[0]
for i in range(K):
    ax_price.plot(X, A[:, i], label=f"Trajectory {i+1}")
ax_price.set_ylabel("Price")
ax_price.set_title("GBM Simulated Trajectories")
ax_price.legend()

# One subplot per trajectory showing its running drawdown
for i in range(K):
    ax = axes[i + 1]
    dd = running_drawdown(A[:, i])
    ax.plot(X, dd, color="firebrick")
    ax.fill_between(X, dd, 0, color="firebrick", alpha=0.3)

    max_dd = dd.min()
    max_dd_idx = dd.argmin()
    ax.scatter(X[max_dd_idx], max_dd, color="black", zorder=5)
    ax.set_ylabel("Drawdown")
    ax.set_title(f"Trajectory {i+1} — Max Drawdown: {max_dd:.2%}")

axes[-1].set_xlabel("Time (years)")
plt.tight_layout()
plt.show()

# Returns Metrics Summary

---

## 1. Arithmetic Returns

**Definition**: The simple percentage change in value between two periods.

$$R_t = \frac{P_t - P_{t-1}}{P_{t-1}}$$

**Properties**

- Easy to compute and interpret
- Best used for **single-period** analysis
- Overstates long-run performance when averaged across periods (ignores compounding)

**Example**: If a stock goes from $100 → $110 → $99, the arithmetic mean return is:
$$\bar{R} = \frac{10\% + (-10\%)}{2} = 0\%$$
But the investor actually **lost money** — this is the limitation.

**Use case**: Daily/monthly return calculations, input for rolling mean computations.

---

## 2. Cumulative Returns

**Definition**: The total return of an asset over a given period, accounting for compounding.

$$R_{cumulative} = \prod_{t=1}^{T}(1 + R_t) - 1$$

In pandas:

```python
cumulative_returns = (1 + returns).cumprod()
```

**Properties**

- Captures the **compounding effect** of returns over time
- Starts at 1.0 (or 0% gain) and grows/shrinks from there
- Always path-dependent — sequence of returns matters (volatility drag)

**Example**: Using the same stock ($100 → $110 → $99):
$$R_{cumulative} = (1 + 0.10) \times (1 - 0.10) - 1 = 1.10 \times 0.90 - 1 = -1\%$$
Correctly reflects the actual loss.

**Use case**: Visualizing total portfolio growth over time, comparing strategies over a full backtest window.

---

## 3. CAGR — Compound Annual Growth Rate

**Definition**: The annualized rate of return that would take a portfolio from its beginning value to its ending value over a given number of years, assuming returns are reinvested.

$$CAGR = \left(\frac{V_{end}}{V_{start}}\right)^{\frac{1}{T}} - 1$$

Where $T$ is the number of years.

**Properties**

- Smooths out volatility — gives a single "steady-state" growth rate
- More meaningful than arithmetic mean for multi-year performance comparison
- Does **not** reflect the volatility experienced along the way (use Sharpe ratio for that)

**Example**: Portfolio grows from $100 to $200 over 7 years:
$$CAGR = \left(\frac{200}{100}\right)^{\frac{1}{7}} - 1 \approx 10.4\%$$

In pandas:

```python
n_years = (returns.index[-1] - returns.index[0]).days / 365.25
cagr = (cumulative_returns.iloc[-1]) ** (1 / n_years) - 1
```

**Use case**: Benchmarking long-run strategy performance, comparing funds/strategies across different time horizons.

---

## 4. Sharpe Ratio

**Definition**: Measures the **risk-adjusted return** of a portfolio — how much excess return is earned per unit of volatility taken.

$$Sharpe = \frac{R_p - R_f}{\sigma_p}$$

Where:

- $R_p$ = annualized portfolio return
- $R_f$ = risk-free rate (e.g. 3-month Treasury bill yield)
- $\sigma_p$ = annualized standard deviation of portfolio returns (volatility)

**Properties**

- Dimensionless — allows comparison across strategies with different scales
- Higher is better: a Sharpe of 1.0 is acceptable, 2.0+ is strong, 3.0+ is exceptional
- Penalizes **both upside and downside** volatility equally (a known limitation)
- Assumes returns are normally distributed — less reliable for strategies with skewed or fat-tailed returns

**Interpretation guide**

| Sharpe Ratio | Assessment                                      |
| ------------ | ----------------------------------------------- |
| < 0          | Strategy loses money relative to risk-free rate |
| 0 – 0.5      | Poor risk-adjusted performance                  |
| 0.5 – 1.0    | Below average                                   |
| 1.0 – 2.0    | Good                                            |
| 2.0 – 3.0    | Very good                                       |
| > 3.0        | Exceptional (rare in practice)                  |

**Example**: Two strategies both return 15% annually:

- Strategy A: volatility = 10% → $Sharpe = \frac{0.15 - 0.05}{0.10} = 1.0$
- Strategy B: volatility = 20% → $Sharpe = \frac{0.15 - 0.05}{0.20} = 0.5$

Strategy A is preferable — same return with half the risk.

**Annualized portfolio return formula**

When working with daily returns, $R_p$ is computed as:

$$R_p = \bar{R}_{daily} \times N$$

Where $N = 252$ (trading days per year). This scales the average daily return up to an annual figure.

**Why volatility uses $N^{0.5}$ instead of $N$**

Volatility (standard deviation) does **not** scale linearly with time — it scales with the **square root of time**. This comes from the statistical property of independent random variables:

$$\sigma_{annual} = \sigma_{daily} \times \sqrt{N}$$

**Intuition**: Variance (spread of outcomes) accumulates linearly over time, but standard deviation is the square root of variance, so it grows as $\sqrt{N}$. Written explicitly:

$$\sigma_{annual}^2 = \sigma_{daily}^2 \times N \implies \sigma_{annual} = \sigma_{daily} \times \sqrt{N} = \sigma_{daily} \times N^{0.5}$$

This is why in the Sharpe formula both components must be annualized consistently:

$$Sharpe = \frac{\bar{R}_{daily} \times N}{\sigma_{daily} \times \sqrt{N}} = \frac{\bar{R}_{daily}}{\sigma_{daily}} \times \sqrt{N}$$

In pandas (annualized, assuming daily returns):

```python
risk_free_rate = 0.05  # 5% annual
tradingdays = 252

excess_returns = returns - risk_free_rate / tradingdays
sharpe = (excess_returns.mean() / excess_returns.std()) * (tradingdays ** 0.5)
```

**Limitation**: The Sharpe ratio penalizes upside volatility the same as downside. The **Sortino ratio** addresses this by only penalizing downside deviation.

**Use case**: Comparing strategies or funds with different return and risk profiles; standard metric in portfolio management and backtesting.

---

## 5. Annualized Volatility

**Definition**: The annualized standard deviation of returns — measures the **dispersion (risk) of returns** over a year. It quantifies how much the returns fluctuate around their mean.

$$\sigma_{annual} = \sigma_{daily} \times \sqrt{N}$$

Where:

- $\sigma_{daily}$ = standard deviation of daily returns
- $N = 252$ = number of trading days per year

**Why $\sqrt{N}$ and not $N$?** See the Sharpe Ratio section above — variance scales linearly with time, so standard deviation scales with $\sqrt{N}$.

**Properties**

- Expressed as a percentage (e.g. 15% annual volatility)
- Higher volatility = higher risk = wider range of possible outcomes
- Does **not** indicate direction — a high-volatility asset can be going up or down sharply
- Is the denominator of the Sharpe ratio — lower volatility for the same return = better risk-adjusted performance

**Interpretation guide**

| Annualized Volatility | Typical Asset Class                               |
| --------------------- | ------------------------------------------------- |
| < 5%                  | Cash, short-term bonds                            |
| 5 – 10%               | Long-term bonds, low-volatility equity strategies |
| 10 – 20%              | Diversified equity portfolios (e.g. S&P500 ~15%)  |
| 20 – 40%              | Individual stocks, sector ETFs                    |
| > 40%                 | Cryptocurrencies, highly leveraged strategies     |

**Example**: S&P500 historical daily volatility ≈ 1%, annualized:
$$\sigma_{annual} = 0.01 \times \sqrt{252} \approx 15.9\%$$

In pandas (annualized, assuming daily returns):

```python
tradingdays = 252
annualized_volatility = returns.std() * (tradingdays ** 0.5)
```

**Rolling volatility** — useful for seeing how risk changes over time:

```python
rolling_vol = returns.rolling(window=tradingdays).std() * (tradingdays ** 0.5)
```

**Relationship to other metrics**

- Used directly in the **Sharpe ratio** as $\sigma_p$
- Combined with CAGR, gives a complete picture: high CAGR + low volatility = ideal strategy
- During market crises (2008, 2020), volatility spikes sharply — this is called **volatility clustering**

**Use case**: Risk measurement, position sizing, strategy comparison, computing Sharpe/Sortino ratios.

---

## Comparison Table

| Metric                    | Accounts for Compounding | Risk-Adjusted | Time Horizon  | Best Used For                          |
| ------------------------- | ------------------------ | ------------- | ------------- | -------------------------------------- |
| **Arithmetic Return**     | No                       | No            | Single period | Daily/monthly analysis, rolling means  |
| **Cumulative Return**     | Yes                      | No            | Full period   | Visualizing total growth over backtest |
| **CAGR**                  | Yes                      | No            | Multi-year    | Annualized benchmarking and comparison |
| **Sharpe Ratio**          | No                       | Yes           | Any           | Risk-adjusted strategy comparison      |
| **Annualized Volatility** | No                       | No            | Any           | Risk measurement, Sharpe denominator   |

---

## Key Relationship

$$CAGR = (1 + R_{cumulative})^{\frac{1}{T}} - 1$$

A strategy with a **cumulative return of 100% over 7 years** has a **CAGR of ~10.4%**, not 14.3% (which would be the naive arithmetic average of 100%/7).

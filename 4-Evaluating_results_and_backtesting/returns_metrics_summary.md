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

## 2. Logarithmic Returns

**Definition**: The natural logarithm of the price ratio between two periods.

$$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1})$$

**Properties**

- Also called **continuously compounded returns** or **log returns**
- **Time-additive**: log returns sum across periods, unlike arithmetic returns which must be multiplied — this makes multi-period aggregation trivial
- Approximately equal to arithmetic returns for small values: $r_t \approx R_t$ when $R_t \ll 1$
- Symmetric: a 10% gain followed by a 10% loss gives the same log return magnitude with opposite signs (not true for arithmetic returns)
- Assumed to be normally distributed in many financial models (e.g. Black-Scholes), making them statistically convenient
- **Not cross-sectionally additive** — you cannot directly sum log returns across different assets in a portfolio (arithmetic returns are used for portfolio aggregation)

**Relationship to arithmetic returns**

$$r_t = \ln(1 + R_t) \quad \Longleftrightarrow \quad R_t = e^{r_t} - 1$$

For multi-period aggregation:
$$r_{[1,T]} = \sum_{t=1}^{T} r_t = \ln\left(\frac{P_T}{P_0}\right)$$

Compare this to arithmetic returns which require:
$$R_{[1,T]} = \prod_{t=1}^{T}(1 + R_t) - 1$$

**Example**: Using the same stock ($100 → $110 → $99):
$$r_1 = \ln\left(\frac{110}{100}\right) \approx 9.53\%, \quad r_2 = \ln\left(\frac{99}{110}\right) \approx -10.54\%$$
$$r_{total} = r_1 + r_2 \approx -1.01\%$$
This correctly reflects the loss and matches the cumulative arithmetic result.

In pandas:

```python
import numpy as np

log_returns = np.log(prices / prices.shift(1))
# or equivalently:
log_returns = np.log(prices).diff()
```

**Use case**: Statistical modelling, option pricing models, time-series analysis, and any scenario where time-additivity simplifies computation.

---

## 3. Cumulative Returns

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

## 4. CAGR — Compound Annual Growth Rate

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

## Key Relationship

$$CAGR = (1 + R_{cumulative})^{\frac{1}{T}} - 1$$

A strategy with a **cumulative return of 100% over 7 years** has a **CAGR of ~10.4%**, not 14.3% (which would be the naive arithmetic average of 100%/7).

---

## 5. Annualized Returns

**Definition**: The scaling of a sub-annual (daily, weekly, or monthly) mean return to an equivalent annual rate, allowing fair comparison across strategies measured over different time windows or at different sampling frequencies.

There are two common annualization approaches depending on whether you treat returns as additive (arithmetic) or multiplicative (geometric/compound).

**Arithmetic annualization** (linear scaling)

$$R_{annual} = \bar{R}_{period} \times N$$

Where:

- $\bar{R}_{period}$ = mean return per period (e.g. average daily return)
- $N$ = number of periods per year

| Frequency | $N$ |
| --------- | --- |
| Daily     | 252 |
| Weekly    | 52  |
| Monthly   | 12  |
| Quarterly | 4   |

This is the simplest approach and is used as the numerator in the **Sharpe ratio**. It assumes returns can be linearly summed — valid as an approximation for small returns over short windows.

**Geometric annualization** (compound scaling)

$$R_{annual} = (1 + \bar{R}_{period})^{N} - 1$$

This approach accounts for compounding: each period's return is reinvested. For longer horizons or larger per-period returns, geometric annualization is more accurate. **CAGR** is the geometric annualization applied to the total cumulative return over a multi-year period.

**Relationship between the two**

For small $\bar{R}_{period}$, the two converge:

$$R_{annual}^{arithmetic} \approx R_{annual}^{geometric} \quad \text{when} \quad \bar{R}_{period} \ll 1$$

For larger returns (or longer compounding windows), arithmetic annualization **overstates** the true compound return because it ignores the drag from volatility.

**Example**: A strategy earns an average daily return of 0.04%:

- Arithmetic: $R_{annual} = 0.0004 \times 252 = 10.08\%$
- Geometric: $R_{annual} = (1.0004)^{252} - 1 \approx 10.62\%$

The difference is small for low daily returns, but grows as the daily return or volatility increases.

In pandas (daily returns):

```python
tradingdays = 252

# Arithmetic annualization (used in Sharpe ratio)
annualized_return_arithmetic = returns.mean() * tradingdays

# Geometric annualization
annualized_return_geometric = (1 + returns.mean()) ** tradingdays - 1
```

**Properties**

- Does **not** account for the path of returns — only the average return per period
- Arithmetic annualization overstates true performance when volatility is high (**volatility drag**)
- Geometric annualization is always $\leq$ arithmetic annualization (Jensen's inequality)
- Neither method accounts for the sequence of returns — that is captured by CAGR, which uses actual start and end portfolio values

**Why arithmetic annualization uses $N$ but volatility uses $\sqrt{N}$**

Mean return scales linearly: if you earn on average $\bar{R}$ per day, you expect $\bar{R} \times N$ over $N$ days. Variance also scales linearly, but standard deviation is the square root of variance, so it scales as $\sqrt{N}$. This asymmetry is why the Sharpe ratio simplifies to:

$$Sharpe = \frac{\bar{R}_{daily} \times N}{\sigma_{daily} \times \sqrt{N}} = \frac{\bar{R}_{daily}}{\sigma_{daily}} \times \sqrt{N}$$

**Relationship to other metrics**

- The **Sharpe ratio** uses arithmetic annualized return in its numerator, consistent with how annualized volatility is scaled by $\sqrt{N}$
- **CAGR** is the correct geometric annualization using actual start/end portfolio values — more accurate than applying geometric scaling to a mean daily return
- **Annualized volatility** uses $\sqrt{N}$ scaling, not $N$, because standard deviation scales with the square root of time

**Use case**: Sharpe/Sortino ratio numerator, normalizing performance across strategies run over different periods, performance reporting.

---

## 6. Sharpe Ratio

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

## 7. Annualized Volatility

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

## 8. Kurtosis

**Definition**: A statistical measure of the **tailedness** of a return distribution — how much probability mass sits in the tails compared to a normal distribution.

$$\kappa = \frac{\frac{1}{N}\displaystyle\sum_{t=1}^{N}(R_t - \bar{R})^4}{\left(\frac{1}{N}\displaystyle\sum_{t=1}^{N}(R_t - \bar{R})^2\right)^2}$$

Since the denominator is the squared variance — and variance is the square of standard deviation ($\sigma^2$) — this is equivalently expressed as:

$$\kappa = \frac{\frac{1}{N}\displaystyle\sum_{t=1}^{N}(R_t - \bar{R})^4}{\sigma^4} = \frac{1}{N}\sum_{t=1}^{N}\left(\frac{R_t - \bar{R}}{\sigma}\right)^4$$

Where $\sigma = \sqrt{\frac{1}{N}\sum_{t=1}^{N}(R_t - \bar{R})^2}$ is the standard deviation of returns. This form makes the interpretation clearer: kurtosis is the **average of the fourth power of standardized returns** (i.e. returns expressed in units of standard deviation). For a normal distribution, this average equals 3.

In practice, **excess kurtosis** is more commonly reported, defined as:

$$\kappa_{excess} = \kappa - 3$$

This centres the measure at zero for a normal distribution, making deviations easier to interpret.

**Properties**

- A normal distribution has kurtosis $\kappa = 3$ and excess kurtosis $= 0$
- **Leptokurtic** ($\kappa_{excess} > 0$): fat tails — extreme returns occur more frequently than a normal distribution predicts (common in financial returns)
- **Platykurtic** ($\kappa_{excess} < 0$): thin tails — fewer extreme events than a normal distribution
- **Mesokurtic** ($\kappa_{excess} = 0$): matches the normal distribution's tail behavior
- High positive excess kurtosis is a warning sign: models assuming normality (e.g. Sharpe ratio, VaR) will **underestimate** the probability of large losses
- Kurtosis captures tail risk that volatility alone misses — two assets can have the same standard deviation but very different kurtosis

**Interpretation guide**

| Excess Kurtosis | Distribution Type  | Implication                                   |
| --------------- | ------------------ | --------------------------------------------- |
| = 0             | Mesokurtic         | Normal tails — standard models apply          |
| > 0             | Leptokurtic        | Fat tails — crash/spike risk underestimated   |
| > 3             | Highly leptokurtic | Extreme events significantly more likely      |
| < 0             | Platykurtic        | Thin tails — returns more bounded than normal |

**By-hand calculation** (excess kurtosis, step by step):

Given daily returns $R_1, R_2, \ldots, R_N$:

1. Compute the mean: $\bar{R} = \frac{1}{N}\sum R_t$
2. Compute the deviations: $d_t = R_t - \bar{R}$
3. Compute the fourth central moment: $m_4 = \frac{1}{N}\sum d_t^4$
4. Compute the variance: $m_2 = \frac{1}{N}\sum d_t^2$
5. Compute kurtosis: $\kappa = \frac{m_4}{m_2^2}$
6. Subtract 3 for excess kurtosis: $\kappa_{excess} = \kappa - 3$

**Example**: S&P 500 daily returns historically exhibit excess kurtosis of roughly **4–6**, meaning large single-day moves (±3–5%) are far more frequent than a normal distribution would predict. This is the "fat tails" phenomenon observed during events like 2008 or March 2020.

In pandas:

```python
# pandas .kurtosis() returns excess kurtosis (Fisher's definition, kurtosis - 3) by default
excess_kurtosis = returns.kurtosis()

# For the raw (Pearson) kurtosis:
raw_kurtosis = returns.kurtosis() + 3

# Rolling kurtosis — useful for detecting regime changes in tail risk:
rolling_kurt = returns.rolling(window=252).kurtosis()
```

**Relationship to other metrics**

- Complements **annualized volatility**: volatility measures spread, kurtosis measures whether that spread comes from many small moves or rare large ones
- A strategy with low volatility but high kurtosis can still suffer catastrophic losses — this is sometimes called **"picking up nickels in front of a steamroller"**
- Combined with **skewness** (asymmetry), kurtosis gives a fuller picture of the return distribution beyond the mean and variance assumed by the Sharpe ratio

**Use case**: Distribution analysis, tail-risk assessment, stress testing, evaluating whether Sharpe ratio assumptions are valid.

---

## 9. Skewness

**Definition**: A statistical measure of the **asymmetry** of a return distribution around its mean — whether returns are skewed towards large gains or large losses.

$$S = \frac{\frac{1}{N}\displaystyle\sum_{t=1}^{N}(R_t - \bar{R})^3}{\sigma^3} = \frac{1}{N}\sum_{t=1}^{N}\left(\frac{R_t - \bar{R}}{\sigma}\right)^3$$

Where $\sigma$ is the standard deviation of returns. Skewness is the **average of the third power of standardized returns** — the cubic power preserves the sign, so it captures the direction of the asymmetry.

**Properties**

- A normal distribution has skewness $S = 0$ (perfectly symmetric)
- **Positive skew** ($S > 0$): the right tail is longer — most returns are below the mean, but occasional large gains pull the average up (e.g. venture capital, trend-following strategies)
- **Negative skew** ($S < 0$): the left tail is longer — most returns are above the mean, but occasional large losses drag the average down (common in equity markets and option-selling strategies)
- Negative skewness is particularly dangerous: it implies that the worst outcomes are more extreme than the best ones — the strategy looks good most of the time but can suffer severe drawdowns
- The Sharpe ratio does **not** distinguish between positive and negative skew — a strategy with negative skew may show an attractive Sharpe ratio while hiding crash risk

**Interpretation guide**

| Skewness       | Distribution Type | Implication                                            |
| -------------- | ----------------- | ------------------------------------------------------ |
| = 0            | Symmetric         | Normal-like — standard models apply                    |
| > 0 (positive) | Right-skewed      | Rare large gains; most returns cluster below the mean  |
| < 0 (negative) | Left-skewed       | Rare large losses; most returns cluster above the mean |
| < −1 or > +1   | Highly skewed     | Strong asymmetry; normality assumption breaks down     |

**By-hand calculation** (step by step):

Given daily returns $R_1, R_2, \ldots, R_N$:

1. Compute the mean: $\bar{R} = \frac{1}{N}\sum R_t$
2. Compute the deviations: $d_t = R_t - \bar{R}$
3. Compute the standard deviation: $\sigma = \sqrt{\frac{1}{N}\sum d_t^2}$
4. Compute the third central moment: $m_3 = \frac{1}{N}\sum d_t^3$
5. Compute skewness: $S = \frac{m_3}{\sigma^3}$

**Example**: S&P 500 daily returns typically exhibit **negative skewness** of around $-0.5$ to $-1.0$. This reflects the well-known asymmetry of equity markets — gains accumulate slowly and losses arrive suddenly (e.g. Black Monday 1987, March 2020).

In pandas:

```python
# pandas .skew() returns the sample skewness (Fisher-Pearson) by default
skewness = returns.skew()

# Rolling skewness — useful for detecting shifts in distribution shape over time:
rolling_skew = returns.rolling(window=252).skew()
```

**Relationship to other metrics**

- Paired with **kurtosis**, skewness completes the description of a distribution's shape beyond mean and variance
- Negative skew + high kurtosis is the most dangerous combination: a strategy that appears stable can suffer rare but catastrophic losses
- The **Sortino ratio** partially addresses negative skewness by penalizing only downside deviations, unlike the Sharpe ratio
- When skewness is significant, the Sharpe ratio should be interpreted with caution — a negatively skewed strategy may show a high Sharpe while carrying hidden tail risk

**Use case**: Distribution analysis, identifying crash-prone strategies, complementing the Sharpe ratio, risk reporting.

---

## 10. Drawdown

**Definition**: The decline in portfolio value from a historical peak to a subsequent trough — measured as a percentage of the peak value.

$$DD_t = \frac{V_t - \max_{s \leq t}(V_s)}{\max_{s \leq t}(V_s)}$$

Where:

- $V_t$ = portfolio value at time $t$
- $\max_{s \leq t}(V_s)$ = the running maximum (highest portfolio value seen up to time $t$)

The result is always $\leq 0$ (or 0% when at a new all-time high).

**Key variants**

- **Drawdown series**: the full time-series of $DD_t$ — shows when and how long the portfolio was underwater
- **Maximum Drawdown (MDD)**: the single worst peak-to-trough decline over the entire period

$$MDD = \min_t(DD_t)$$

- **Drawdown duration**: how long it took to recover back to the previous peak (can be months or years)

**Properties**

- Expressed as a negative percentage (e.g. −30% means the portfolio fell 30% from its peak)
- Measures **realized downside risk** — unlike volatility, it is path-dependent and directly reflects the worst investor experience
- Does **not** penalize upside moves — only tracks declines from peaks
- A drawdown ends only when the portfolio **fully recovers** to its previous high; partial recoveries still count as being in drawdown
- Long drawdown durations are psychologically damaging — investors often abandon strategies before recovery

**Interpretation guide**

| Max Drawdown | Implication                                          |
| ------------ | ---------------------------------------------------- |
| 0% – 10%     | Very low risk strategy (e.g. short-term bonds)       |
| 10% – 20%    | Moderate — typical for diversified portfolios        |
| 20% – 40%    | Significant — common for equity-only strategies      |
| 40% – 60%    | Severe — seen in aggressive or concentrated bets     |
| > 60%        | Extreme — near-catastrophic for leveraged strategies |

**Example**: A portfolio grows: $100 → $150 → $90 → $120

- Peak after period 1: $150
- Trough in period 2: $90
- MDD = $\frac{90 - 150}{150} = -40\%$
- The portfolio is still in drawdown at $120 (has not yet recovered to $150)

**By-hand calculation** (step by step):

Given a portfolio value series $V_1, V_2, \ldots, V_T$:

1. Compute the running maximum: $M_t = \max(V_1, V_2, \ldots, V_t)$
2. Compute the drawdown at each point: $DD_t = \frac{V_t - M_t}{M_t}$
3. The maximum drawdown is: $MDD = \min(DD_1, DD_2, \ldots, DD_T)$

In pandas (using cumulative returns):

```python
# Compute cumulative returns first
cumulative_returns = (1 + returns).cumprod()

# Running peak (rolling maximum)
running_max = cumulative_returns.cummax()

# Drawdown series
drawdown = (cumulative_returns - running_max) / running_max

# Maximum drawdown (single worst value)
max_drawdown = drawdown.min()
```

Plotting the drawdown series:

```python
import matplotlib.pyplot as plt

drawdown.plot(title='Drawdown', ylabel='Drawdown', color='red')
plt.fill_between(drawdown.index, drawdown, 0, alpha=0.3, color='red')
plt.show()
```

**Calmar Ratio** — a common companion metric that relates return to drawdown risk:

$$Calmar = \frac{CAGR}{|MDD|}$$

Higher is better. A Calmar of 1.0 means the strategy's annual growth rate equals its worst historical loss — a reasonable baseline.

**Relationship to other metrics**

- Complements the **Sharpe ratio**: two strategies can have the same Sharpe but very different drawdown profiles — a strategy with long, deep drawdowns is harder to stick with even if it ultimately recovers
- Directly linked to **negative skewness**: strategies with negative skew tend to have sudden, severe drawdowns (the left-tail events manifest as sharp peak-to-trough moves)
- High **kurtosis** amplifies drawdown severity — fat-tailed strategies can experience single-day drops that immediately create large drawdowns
- **Volatility** and drawdown are related but not the same: a high-volatility strategy recovers faster on average, while a low-volatility strategy with negative skew can enter a deep, slow drawdown

**Use case**: Strategy risk reporting, position sizing, evaluating investor experience, computing Calmar ratio, stress testing.

---

## 11. Sortino Ratio

**Definition**: A risk-adjusted return metric like the Sharpe ratio, but it only penalizes **downside** volatility — volatility from returns that fall below a target threshold (usually zero or the risk-free rate).

$$Sortino = \frac{R_p - R_f}{\sigma_{downside}}$$

Where:

- $R_p$ = annualized portfolio return
- $R_f$ = risk-free rate (or minimum acceptable return)
- $\sigma_{downside}$ = annualized **downside deviation** — standard deviation computed using only returns below the threshold

**Downside deviation formula**:

$$\sigma_{downside} = \sqrt{\frac{1}{N}\sum_{t=1}^{N}\min(R_t - R_f,\ 0)^2}$$

Only returns below the threshold $R_f$ contribute to the sum. Positive excess returns are treated as zero — they do not increase the penalty.

**Why it exists — the Sharpe ratio's blind spot**

The Sharpe ratio uses total standard deviation as its risk measure, which penalizes **upside volatility equally to downside volatility**. A strategy that occasionally has large gains will be punished by Sharpe, even though large gains are desirable. The Sortino ratio fixes this by only measuring the volatility that investors actually care about: losses.

**Properties**

- Always $\geq$ Sharpe ratio (because $\sigma_{downside} \leq \sigma_{total}$)
- More informative for **asymmetric strategies** — e.g. trend-following, options buying — where upside volatility is a feature, not a bug
- For symmetric, normally distributed returns, Sortino and Sharpe tell the same story
- The gap between Sortino and Sharpe is itself informative: a large gap means the strategy has significant upside volatility (positively skewed) — which is generally good

**Interpretation guide**

| Sortino Ratio | Assessment                        |
| ------------- | --------------------------------- |
| < 0           | Loses money relative to threshold |
| 0 – 1.0       | Poor to below average             |
| 1.0 – 2.0     | Good                              |
| 2.0 – 3.0     | Very good                         |
| > 3.0         | Exceptional                       |

Note: Sortino thresholds are generally set higher than Sharpe thresholds because Sortino will always produce a higher number for the same strategy.

**Example**: Two strategies, both with annualized return = 12% and risk-free rate = 4%:

- Strategy A: $\sigma_{total} = 15\%$, $\sigma_{downside} = 12\%$ → $Sharpe = 0.53$, $Sortino = 0.67$
- Strategy B: $\sigma_{total} = 15\%$, $\sigma_{downside} = 6\%$ → $Sharpe = 0.53$, $Sortino = 1.33$

Both have identical Sharpe ratios, but Strategy B has much less downside risk — the Sortino ratio correctly identifies it as the better strategy.

In pandas (annualized, assuming daily returns):

```python
tradingdays = 252
risk_free_rate = 0.05  # 5% annual

excess_returns = returns - risk_free_rate / tradingdays

# Only use returns below the threshold for downside deviation
downside_returns = excess_returns.copy()
downside_returns[downside_returns > 0] = 0

downside_deviation = downside_returns.std() * (tradingdays ** 0.5)
annualized_excess_return = excess_returns.mean() * tradingdays

sortino = annualized_excess_return / downside_deviation
```

**Relationship to other metrics**

- **vs Sharpe**: Sortino is strictly better for negatively skewed or asymmetric strategies; they converge for normally distributed returns
- **vs Drawdown**: Sortino captures frequent small losses; drawdown captures the single worst sustained decline — both are needed for a complete picture
- **vs Skewness**: a high Sortino relative to Sharpe implies positive skew (upside volatility dominates); a low Sortino relative to Sharpe implies negative skew (downside volatility dominates)

**Use case**: Evaluating strategies with asymmetric return profiles, comparing trend-following or momentum strategies, any context where penalizing upside volatility is inappropriate.

---

## 12. Calmar Ratio

**Definition**: Measures risk-adjusted return by relating the annualized growth rate (CAGR) to the worst historical loss (Maximum Drawdown) — it answers: _"how much annual return am I getting per unit of maximum drawdown risk?"_

$$Calmar = \frac{CAGR}{|MDD|}$$

Where:

- $CAGR$ = compound annual growth rate over the period
- $|MDD|$ = absolute value of the maximum drawdown (expressed as a positive number)

**Properties**

- Higher is better — a Calmar of 1.0 means the strategy earns as much per year as it lost at its worst point
- Naturally penalizes strategies that suffer deep, sudden crashes even if they recover
- Typically computed over a **3-year rolling window**, though the full period is also common
- Unlike Sharpe/Sortino, Calmar is based on a **single worst event** rather than average volatility — making it sensitive to the time period chosen

**Interpretation guide**

| Calmar Ratio | Assessment                                             |
| ------------ | ------------------------------------------------------ |
| < 0.5        | Poor — drawdown risk far outweighs annual return       |
| 0.5 – 1.0    | Below average                                          |
| 1.0 – 2.0    | Good — standard for well-run CTA/hedge fund strategies |
| 2.0 – 3.0    | Very good                                              |
| > 3.0        | Exceptional — rare outside of short, favorable periods |

**Example**: A strategy with CAGR = 15% and MDD = −25%:

$$Calmar = \frac{0.15}{0.25} = 0.60$$

This is below average — the worst loss was nearly 2× the annual return. A stronger strategy might achieve CAGR = 20%, MDD = −10%:

$$Calmar = \frac{0.20}{0.10} = 2.0$$

In pandas:

```python
import numpy as np

# Assumes cumulative_returns is already computed as (1 + returns).cumprod()
n_years = (returns.index[-1] - returns.index[0]).days / 365.25
cagr = cumulative_returns.iloc[-1] ** (1 / n_years) - 1

running_max = cumulative_returns.cummax()
drawdown = (cumulative_returns - running_max) / running_max
max_drawdown = drawdown.min()  # negative number

calmar = cagr / abs(max_drawdown)
```

**Key limitation — recency and period sensitivity**

The Calmar ratio depends heavily on whether a major crash falls within the measurement window. A strategy evaluated from 2010–2019 (no major crash) will show a very different Calmar than the same strategy evaluated from 2008–2019 (includes the financial crisis). Always check the time period when comparing Calmar ratios across strategies.

**Relationship to other metrics**

- **vs Sharpe**: Sharpe uses average volatility; Calmar uses the single worst drawdown — Calmar is more relevant for investors who cannot psychologically or financially tolerate large peak-to-trough losses
- **vs Sortino**: Sortino penalizes frequent small losses; Calmar penalizes the single worst sustained loss — they capture different dimensions of downside risk
- **vs Drawdown**: Calmar contextualizes the drawdown relative to return — a 30% drawdown is acceptable for a strategy returning 40%/year (Calmar ≈ 1.3), but alarming for one returning 5%/year (Calmar ≈ 0.17)

**Use case**: Evaluating managed futures, hedge funds, and systematic trading strategies where avoiding large drawdowns is a primary objective; comparing strategies over the same time window.

---

## Comparison Table

| Metric                    | Accounts for Compounding | Risk-Adjusted | Time Horizon  | Best Used For                                    |
| ------------------------- | ------------------------ | ------------- | ------------- | ------------------------------------------------ |
| **Arithmetic Return**     | No                       | No            | Single period | Daily/monthly analysis, rolling means            |
| **Logarithmic Return**    | Yes (time-additive)      | No            | Single period | Statistical modelling, time-series analysis      |
| **Cumulative Return**     | Yes                      | No            | Full period   | Visualizing total growth over backtest           |
| **CAGR**                  | Yes                      | No            | Multi-year    | Annualized benchmarking and comparison           |
| **Annualized Returns**    | No (arithmetic) / Yes (geometric) | No | Any      | Normalizing returns for comparison, Sharpe numerator |
| **Sharpe Ratio**          | No                       | Yes           | Any           | Risk-adjusted strategy comparison                |
| **Annualized Volatility** | No                       | No            | Any           | Risk measurement, Sharpe denominator             |
| **Kurtosis**              | No                       | No            | Any           | Tail-risk assessment, distribution analysis      |
| **Skewness**              | No                       | No            | Any           | Asymmetry analysis, hidden crash-risk detection  |
| **Drawdown**              | Yes                      | No            | Full period   | Worst-loss assessment, investor experience       |
| **Sortino Ratio**         | No                       | Yes           | Any           | Risk-adjusted return, penalizes downside only    |
| **Calmar Ratio**          | Yes                      | Yes           | Full period   | Return vs worst drawdown, crash-prone strategies |

---

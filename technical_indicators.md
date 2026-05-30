# Technical Indicators

Technical indicators are mathematical calculations based on a security's price, volume, or open interest. Traders use them to identify trends, momentum, volatility, and potential reversal points. They are commonly grouped into four families: **trend**, **momentum**, **volatility**, and **volume** indicators.

Notation used below:

- $t$ = the current time step (e.g., today's bar in a daily chart, or the current minute in an intraday chart).
- $i$ = an index variable used inside sums to iterate over past bars (e.g., $i = 0$ is the current bar, $i = 1$ the previous one, etc.).
- $P_t$ = closing price at time $t$ (the last traded price of the bar).
- $O_t, H_t, L_t, C_t$ = open, high, low and close prices of the bar at time $t$.
- $V_t$ = volume traded during bar $t$ (number of shares/contracts exchanged).
- $n$ = **lookback period** (window length), i.e. how many past bars the indicator considers. Common choices are 9, 14, 20, 26, 50, 200.
- $\sigma_n(X_t)$ = standard deviation of the series $X$ over the last $n$ bars (a measure of dispersion / volatility).
- $\text{SMA}_n(X_t)$, $\text{EMA}_n(X_t)$ = the Simple / Exponential Moving Average of series $X$ over $n$ bars.

---

## 1. Trend Indicators

### 1.1 Simple Moving Average (SMA)

**What it is:** The unweighted mean of the last $n$ prices. The most basic trend smoother.

**Formula:**
$$\text{SMA}_t(n) = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}$$

Where:

- $\text{SMA}_t(n)$ = the moving average value at time $t$ using the last $n$ bars.
- $P_{t-i}$ = the closing price $i$ bars ago ($i=0$ is today, $i=1$ is yesterday, …, $i=n-1$ is the oldest bar in the window).
- $\sum_{i=0}^{n-1}$ = sum across the $n$ most recent bars.
- $\frac{1}{n}$ = arithmetic mean: every bar in the window has equal weight.

**Use:** Identify trend direction (price above SMA → uptrend). Crossovers between a short SMA (e.g., 50) and a long SMA (e.g., 200) generate "golden cross" (bullish) and "death cross" (bearish) signals.

---

### 1.2 Exponential Moving Average (EMA)

**What it is:** A weighted moving average that gives more importance to recent prices, reacting faster than the SMA.

**Formula:**
$$\text{EMA}_t = \alpha \cdot P_t + (1 - \alpha) \cdot \text{EMA}_{t-1}, \quad \alpha = \frac{2}{n + 1}$$

Where:

- $\text{EMA}_t$ = current value of the EMA (recursive: depends on yesterday's EMA).
- $\text{EMA}_{t-1}$ = previous bar's EMA value (the recursion is usually seeded with an SMA of the first $n$ values).
- $P_t$ = current closing price.
- $\alpha$ = **smoothing factor**, a number between 0 and 1 that controls how much weight is given to the most recent price. Larger $\alpha$ → more reactive, less smoothing.
- $n$ = period; the formula $\alpha = 2/(n+1)$ is the standard convention so that an EMA of period $n$ has a center of mass comparable to an SMA of the same period.

**Use:** Same as SMA but more responsive. Forms the building block of MACD and many trend-following systems.

---

### 1.3 Moving Average Convergence Divergence (MACD)

**What it is:** A momentum/trend hybrid measuring the relationship between two EMAs.

**Formula:**
$$\text{MACD}_t = \text{EMA}_{12}(P_t) - \text{EMA}_{26}(P_t)$$
$$\text{Signal}_t = \text{EMA}_9(\text{MACD}_t)$$
$$\text{Histogram}_t = \text{MACD}_t - \text{Signal}_t$$

Where:

- $\text{EMA}_{12}(P_t)$ = fast EMA of closing prices over 12 bars (reacts quickly to price changes).
- $\text{EMA}_{26}(P_t)$ = slow EMA of closing prices over 26 bars (smoother, slower).
- $\text{MACD}_t$ = **MACD line** — the gap between fast and slow EMA. Positive value → short-term momentum is above long-term; negative → below.
- $\text{Signal}_t$ = **signal line**, a 9-bar EMA of the MACD line itself; acts as a smoother trigger for entries/exits.
- $\text{Histogram}_t$ = bar chart of the difference between MACD and signal; visualizes how fast momentum is accelerating or decelerating.

**Use:** Bullish when MACD crosses above the signal line; bearish on the opposite cross. Divergence between MACD and price often warns of trend exhaustion.

---

### 1.4 Average Directional Index (ADX)

**What it is:** Measures the **strength** of a trend (not its direction), on a 0–100 scale, derived from the +DI and −DI directional indicators.

**Formula (simplified):** Smoothed average of $|{+DI} - {-DI}| / ({+DI} + {-DI}) \times 100$ over $n$ periods (typically 14).

Where:

- $+DI$ = **Positive Directional Indicator**, derived from the share of upward price moves ($H_t - H_{t-1}$ when positive) smoothed over $n$ bars. It quantifies bullish pressure.
- $-DI$ = **Negative Directional Indicator**, the equivalent for downward moves ($L_{t-1} - L_t$ when positive). It quantifies bearish pressure.
- $|{+DI} - {-DI}|$ = absolute difference between bullish and bearish pressure — large when one side dominates (strong trend), small when they are balanced (ranging market).
- ${+DI} + {-DI}$ = total directional movement (normalization factor).
- Multiplying by 100 puts ADX on a 0–100 scale; the whole expression is then smoothed (typically with Wilder's smoothing).

**Use:** ADX > 25 indicates a strong trend; ADX < 20 indicates a weak/ranging market. Often used to filter out trend-following signals during chop.

---

### 1.5 Parabolic SAR (Stop and Reverse)

**What it is:** Plots dots above/below price that trail the trend and flip when the trend reverses.

**Formula:** $\text{SAR}_{t+1} = \text{SAR}_t + AF \cdot (\text{EP} - \text{SAR}_t)$

Where:

- $\text{SAR}_t$ = the current SAR (Stop And Reverse) dot value.
- $\text{SAR}_{t+1}$ = the SAR value projected for the next bar.
- $\text{EP}$ = **Extreme Point** — the highest high reached during the current uptrend (or lowest low during a downtrend). Updated whenever a new extreme is seen.
- $AF$ = **Acceleration Factor**, starting at 0.02 and increased by 0.02 each time a new EP is made, capped at 0.20. Higher $AF$ → SAR moves toward price faster, tightening the trailing stop.

**Use:** Trailing stop-loss tool and trend reversal signal.

---

## 2. Momentum Indicators

### 2.1 Relative Strength Index (RSI)

**What it is:** Oscillator measuring the speed and magnitude of recent price changes, bounded between 0 and 100.

**Formula:**
$$\text{RS} = \frac{\text{Average Gain over } n}{\text{Average Loss over } n}, \quad \text{RSI} = 100 - \frac{100}{1 + \text{RS}}$$

Where:

- **Gain** at bar $i$ = $\max(P_i - P_{i-1},\ 0)$ — the positive price change, or 0 if the price went down.
- **Loss** at bar $i$ = $\max(P_{i-1} - P_i,\ 0)$ — the magnitude of the negative price change (always taken as a positive number), or 0 if the price went up.
- **Average Gain / Average Loss** = the mean (or Wilder's smoothed average) of gains and losses over the last $n$ bars.
- $\text{RS}$ = **Relative Strength**: ratio of average gain to average loss. $\text{RS} > 1$ means up-moves dominate.
- $\text{RSI}$ = the relative strength rescaled to a 0–100 range. The transformation $100 - 100/(1 + \text{RS})$ is just a way of mapping $[0, \infty)$ to $[0, 100]$.

Typically $n = 14$.

**Use:** RSI > 70 → overbought (possible pullback); RSI < 30 → oversold (possible bounce). Divergence with price signals weakening momentum.

---

### 2.2 Stochastic Oscillator

**What it is:** Compares the current close to the high–low range over the last $n$ periods.

**Formula:**
$$\%K_t = 100 \cdot \frac{C_t - \min(L_{t-n+1..t})}{\max(H_{t-n+1..t}) - \min(L_{t-n+1..t})}$$
$$\%D_t = \text{SMA}_3(\%K_t)$$

Where:

- $C_t$ = current closing price.
- $\min(L_{t-n+1..t})$ = the **lowest low** observed during the last $n$ bars (the floor of the recent range).
- $\max(H_{t-n+1..t})$ = the **highest high** observed during the last $n$ bars (the ceiling of the recent range).
- The numerator measures how far the close sits above the recent floor; the denominator is the size of the recent range. The ratio tells us where, percentage-wise, the close lies inside that range.
- $\%K_t$ = **fast stochastic line**, in $[0, 100]$. A value of 100 means the close equals the period's high; 0 means it equals the period's low.
- $\%D_t$ = **slow stochastic line** — a 3-bar SMA of $\%K$ used as a signal line.

**Use:** Above 80 = overbought, below 20 = oversold. %K crossing %D generates trade signals.

---

### 2.3 Rate of Change (ROC)

**What it is:** Percentage change in price between the current price and the price $n$ periods ago.

**Formula:**
$$\text{ROC}_t = \frac{P_t - P_{t-n}}{P_{t-n}} \times 100$$

Where:

- $P_t$ = current closing price.
- $P_{t-n}$ = closing price $n$ bars ago (the reference point).
- $P_t - P_{t-n}$ = absolute price change over the period.
- Dividing by $P_{t-n}$ normalizes it into a relative change; multiplying by 100 expresses it as a percentage.

**Use:** Positive ROC = upward momentum; zero-line crosses can act as entry/exit signals.

---

### 2.4 Commodity Channel Index (CCI)

**What it is:** Measures how far the typical price has deviated from its moving average, normalized by mean absolute deviation.

**Formula:**
$$\text{TP}_t = \frac{H_t + L_t + C_t}{3}, \quad \text{CCI}_t = \frac{\text{TP}_t - \text{SMA}_n(\text{TP})}{0.015 \cdot \text{MAD}_n(\text{TP})}$$

Where:

- $\text{TP}_t$ = **Typical Price**, the average of high, low and close for the bar — a more representative single value than just the close.
- $\text{SMA}_n(\text{TP})$ = simple moving average of the typical price over $n$ bars (the "normal" level).
- $\text{MAD}_n(\text{TP})$ = **Mean Absolute Deviation** of TP from its SMA over $n$ bars, i.e. $\frac{1}{n}\sum_{i=0}^{n-1} |\text{TP}_{t-i} - \text{SMA}_n(\text{TP})|$. It plays the role of a volatility scaler (a robust alternative to standard deviation).
- $0.015$ = an empirical constant chosen by Lambert (CCI's creator) so that roughly 70–80 % of values fall within $\pm 100$.

**Use:** Values above +100 suggest overbought / strong uptrend; below −100 suggest oversold / strong downtrend.

---

### 2.5 Williams %R

**What it is:** Inverted stochastic oscillator scaled to $[-100, 0]$.

**Formula:**
$$\%R_t = -100 \cdot \frac{\max(H_{t-n+1..t}) - C_t}{\max(H_{t-n+1..t}) - \min(L_{t-n+1..t})}$$

Where:

- $\max(H_{t-n+1..t})$ = highest high over the last $n$ bars.
- $\min(L_{t-n+1..t})$ = lowest low over the last $n$ bars.
- The numerator measures how far the close sits **below** the recent high.
- The denominator is the total range. The ratio is in $[0, 1]$; the leading $-100$ flips it into $[-100, 0]$, where 0 means the close is at the period's high and $-100$ means it's at the period's low.

**Use:** Above −20 = overbought, below −80 = oversold.

---

## 3. Volatility Indicators

### 3.1 Bollinger Bands

**What it is:** A moving average envelope using standard deviation to define dynamic upper/lower bands.

**Formula:**
$$\text{Middle}_t = \text{SMA}_n(P_t)$$
$$\text{Upper}_t = \text{Middle}_t + k \cdot \sigma_n(P_t), \quad \text{Lower}_t = \text{Middle}_t - k \cdot \sigma_n(P_t)$$

Where:

- $\text{Middle}_t$ = the centerline, an $n$-period SMA of the close (the "fair" recent average).
- $\sigma_n(P_t)$ = **standard deviation** of the last $n$ closing prices — the statistical measure of how dispersed prices are around their average.
- $k$ = a multiplier that controls band width. With $k = 2$, roughly 95 % of values should lie inside the bands under a normal distribution.
- $\text{Upper}_t / \text{Lower}_t$ = volatility-adjusted envelopes that widen in turbulent markets and contract in calm ones.

Typically $n = 20$, $k = 2$.

**Use:** Price touching the upper band suggests overbought; touching the lower suggests oversold. Band "squeeze" (narrow bands) often precedes large breakouts.

---

### 3.2 Average True Range (ATR)

**What it is:** Measures average volatility based on the true price range, without indicating direction.

**Formula:**
$$\text{TR}_t = \max(H_t - L_t,\ |H_t - C_{t-1}|,\ |L_t - C_{t-1}|)$$
$$\text{ATR}_t = \frac{1}{n}\sum_{i=0}^{n-1} \text{TR}_{t-i} \quad \text{(or Wilder's smoothing)}$$

Where:

- $H_t - L_t$ = the current bar's range (intraday volatility).
- $|H_t - C_{t-1}|$ = the gap between today's high and yesterday's close — captures upside overnight gaps.
- $|L_t - C_{t-1}|$ = the gap between today's low and yesterday's close — captures downside overnight gaps.
- $\text{TR}_t$ = **True Range**, the largest of these three distances; it ensures gaps between sessions are accounted for.
- $\text{ATR}_t$ = **Average True Range** over $n$ bars. _Wilder's smoothing_ is a recursive variant: $\text{ATR}_t = \frac{(n-1)\cdot \text{ATR}_{t-1} + \text{TR}_t}{n}$, equivalent to an EMA with $\alpha = 1/n$.

**Use:** Position sizing, setting stop-losses (e.g., stop at $2 \times \text{ATR}$ below entry), and gauging market volatility regimes.

---

### 3.3 Keltner Channels

**What it is:** Volatility envelope built around an EMA, using ATR for the band width.

**Formula:**
$$\text{Upper}_t = \text{EMA}_n(P_t) + m \cdot \text{ATR}_n, \quad \text{Lower}_t = \text{EMA}_n(P_t) - m \cdot \text{ATR}_n$$

Where:

- $\text{EMA}_n(P_t)$ = exponential moving average of the close, used here as the centerline (smoother and more reactive than Bollinger's SMA center).
- $\text{ATR}_n$ = the $n$-period Average True Range — provides the _volatility-based_ band width (unlike Bollinger Bands, which use standard deviation of prices).
- $m$ = ATR multiplier controlling band width; larger $m$ → wider channel, fewer band touches.

Typically $n = 20$, $m = 2$.

**Use:** Trend confirmation and breakout detection; often combined with Bollinger Bands to spot squeezes.

---

## 4. Volume Indicators

### 4.1 On-Balance Volume (OBV)

**What it is:** Cumulative volume flow that adds volume on up days and subtracts on down days.

**Formula:**

$$
\text{OBV}_t =
\begin{cases}
\text{OBV}_{t-1} + V_t & \text{if } C_t > C_{t-1} \\
\text{OBV}_{t-1} - V_t & \text{if } C_t < C_{t-1} \\
\text{OBV}_{t-1} & \text{if } C_t = C_{t-1}
\end{cases}
$$

Where:

- $\text{OBV}_t$ = the running total at bar $t$. Its absolute level is meaningless; only its _direction_ and _slope_ matter.
- $V_t$ = volume of bar $t$ (added on up days, subtracted on down days, ignored on flat days).
- Comparing $C_t$ to $C_{t-1}$ classifies each bar as accumulation (up) or distribution (down).

**Use:** Confirms price trends; OBV divergence from price often precedes a reversal.

---

### 4.2 Volume Weighted Average Price (VWAP)

**What it is:** Average price weighted by traded volume, typically reset daily.

**Formula:**
$$\text{VWAP}_t = \frac{\sum_{i=1}^{t} P_i \cdot V_i}{\sum_{i=1}^{t} V_i}$$

Where:

- $P_i$ = the representative price of bar $i$, typically the **typical price** $(H_i + L_i + C_i)/3$.
- $V_i$ = the volume traded in bar $i$.
- $P_i \cdot V_i$ = the cash value (notional) exchanged during bar $i$.
- $\sum_{i=1}^{t} P_i \cdot V_i$ = cumulative cash value since the session start.
- $\sum_{i=1}^{t} V_i$ = cumulative volume since the session start.
- The ratio gives the average price at which one unit of volume changed hands today — a true volume-weighted average.

**Use:** Benchmark for execution quality; intraday traders treat VWAP as dynamic support/resistance and a fair-value reference.

---

### 4.3 Accumulation/Distribution Line (A/D)

**What it is:** Combines price and volume to measure whether a security is being accumulated (bought) or distributed (sold).

**Formula:**
$$\text{MFM}_t = \frac{(C_t - L_t) - (H_t - C_t)}{H_t - L_t}, \quad \text{MFV}_t = \text{MFM}_t \cdot V_t$$
$$\text{A/D}_t = \text{A/D}_{t-1} + \text{MFV}_t$$

Where:

- $\text{MFM}_t$ = **Money Flow Multiplier**, a number in $[-1, +1]$ that describes where the close fell inside the bar's range: $+1$ if the close equals the high (full buying pressure), $-1$ if it equals the low (full selling pressure), 0 if it closed at the midpoint.
- $\text{MFV}_t$ = **Money Flow Volume** — the multiplier scaled by the bar's volume, so high-volume bars contribute more.
- $\text{A/D}_t$ = the running cumulative sum of MFV; like OBV, only its _slope_ matters, not its absolute level.

**Use:** Rising A/D with rising price confirms uptrend; divergence warns of weakening participation.

---

### 4.4 Chaikin Money Flow (CMF)

**What it is:** Sum of Money Flow Volume over $n$ periods divided by total volume; oscillates around zero.

**Formula:**
$$\text{CMF}_t(n) = \frac{\sum_{i=0}^{n-1} \text{MFV}_{t-i}}{\sum_{i=0}^{n-1} V_{t-i}}$$

Where:

- $\text{MFV}_{t-i}$ = Money Flow Volume (see A/D Line above) of bar $t-i$.
- $V_{t-i}$ = total volume of bar $t-i$.
- The numerator is the net buying/selling money flow over the last $n$ bars.
- The denominator is the total volume over those same $n$ bars (normalization).
- The result is bounded in $[-1, +1]$: close to $+1$ → almost all volume happened on bars closing near their highs (strong buying); close to $-1$ → opposite.

**Use:** CMF > 0 suggests buying pressure; CMF < 0 suggests selling pressure.

---

## 5. Support / Resistance & Other Common Tools

### 5.1 Fibonacci Retracement

**What it is:** Horizontal levels drawn at key Fibonacci ratios (23.6%, 38.2%, 50%, 61.8%, 78.6%) between a swing high and swing low.

**Use:** Identify potential pullback support/resistance levels in a trend.

---

### 5.2 Ichimoku Cloud (Ichimoku Kinkō Hyō)

**What it is:** A multi-component indicator giving trend, momentum, and support/resistance at a glance.

**Components:**

- **Tenkan-sen** ("conversion line") = $(\max H_9 + \min L_9)/2$ — midpoint of the 9-bar range; the fast trend reference.
- **Kijun-sen** ("base line") = $(\max H_{26} + \min L_{26})/2$ — midpoint of the 26-bar range; the slower trend reference, often used as a trailing support/resistance.
- **Senkou Span A** ("leading span A") = $(\text{Tenkan} + \text{Kijun})/2$, plotted **26 periods into the future**. Forms one edge of the cloud.
- **Senkou Span B** ("leading span B") = $(\max H_{52} + \min L_{52})/2$, plotted **26 periods into the future**. The other edge of the cloud. The shaded area between Span A and Span B is the **Kumo (cloud)**.
- **Chikou Span** ("lagging span") = the current close $C_t$, plotted **26 periods into the past**. Used to compare current price with past price action.

Where $\max H_k$ / $\min L_k$ denote the highest high and lowest low over the last $k$ bars. "Plotted ahead/behind" means the value computed at time $t$ is drawn on the chart at time $t+26$ or $t-26$.

**Use:** Price above the cloud = bullish trend; below = bearish. The cloud itself acts as dynamic support/resistance.

---

### 5.3 Pivot Points

**What it is:** Predefined intraday support/resistance levels derived from the previous session's H, L, C.

**Formula (classic):**
$$P = \frac{H + L + C}{3}, \quad R_1 = 2P - L, \quad S_1 = 2P - H$$
$$R_2 = P + (H - L), \quad S_2 = P - (H - L)$$

Where:

- $H, L, C$ = high, low and close of the **previous** trading session (e.g., yesterday's daily bar when computing today's intraday pivots).
- $P$ = **pivot point**, the central reference level (average of yesterday's H, L, C).
- $R_1, R_2$ = first and second **resistance** levels above $P$.
- $S_1, S_2$ = first and second **support** levels below $P$.
- $H - L$ = the previous session's range; wider ranges give wider pivot spacings.

**Use:** Common reference levels for day traders to plan entries, exits, and stops.

---

## Quick Reference Summary

| Indicator        | Family           | Typical Period | Primary Use                   |
| ---------------- | ---------------- | -------------- | ----------------------------- |
| SMA / EMA        | Trend            | 20, 50, 200    | Trend direction, crossovers   |
| MACD             | Trend / Momentum | 12, 26, 9      | Momentum shifts, crossovers   |
| ADX              | Trend strength   | 14             | Filter trending vs. ranging   |
| Parabolic SAR    | Trend            | 0.02, 0.20     | Trailing stop / reversal      |
| RSI              | Momentum         | 14             | Overbought / oversold         |
| Stochastic       | Momentum         | 14, 3          | Overbought / oversold         |
| ROC              | Momentum         | 10–14          | Momentum strength             |
| CCI              | Momentum         | 20             | Cyclical extremes             |
| Williams %R      | Momentum         | 14             | Overbought / oversold         |
| Bollinger Bands  | Volatility       | 20, 2σ         | Volatility & mean reversion   |
| ATR              | Volatility       | 14             | Stops, position sizing        |
| Keltner Channels | Volatility       | 20, 2×ATR      | Breakouts, trend              |
| OBV              | Volume           | —              | Trend confirmation            |
| VWAP             | Volume           | Intraday       | Execution benchmark, S/R      |
| A/D Line         | Volume           | —              | Accumulation vs. distribution |
| CMF              | Volume           | 20             | Buying / selling pressure     |
| Fibonacci        | S/R              | —              | Retracement levels            |
| Ichimoku         | All-in-one       | 9, 26, 52      | Trend, momentum, S/R          |
| Pivot Points     | S/R              | Daily          | Intraday levels               |

---

## Practical Notes

- **No indicator is predictive on its own.** Most traders combine indicators from different families (e.g., a trend filter + a momentum trigger + a volatility-based stop).
- **Beware of redundancy.** Stacking several momentum oscillators (RSI + Stochastic + Williams %R) often gives correlated signals rather than independent confirmation.
- **Parameter tuning matters.** Default periods (14, 20, 50, 200) are conventions, not optima — always validate on out-of-sample data.
- **Indicators lag.** They are derived from past prices; in machine-learning and reinforcement-learning pipelines they are typically used as engineered features, not as standalone signals.

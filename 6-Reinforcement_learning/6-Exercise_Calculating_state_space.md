# Exercise 2: Calculating a State Space

s
This exercise is intended to help you understand the concept of state spaces in financial markets, by manually constructing a state space for given time steps using provided market data. Assume that all financial data and technical indicators are included as features of our state space. Assume all values can be rounded to integers for our state space representation.

---

## 1. Fill in the SMA and RSI Columns for T=5 to T=9

| T   | Close Price | Volume | 5-Day SMA of Close Price | 5-Day RSI of Close Price |
| --- | ----------- | ------ | ------------------------ | ------------------------ |
| 0   | 100         | 1200   |                          |                          |
| 1   | 102         | 1350   |                          |                          |
| 2   | 101         | 1400   |                          |                          |
| 3   | 104         | 1500   |                          |                          |
| 4   | 103         | 1250   | 102                      |                          |
| 5   | 106         | 1100   | 103.2                    | 80                       |
| 6   | 107         | 1400   | 104.2                    | 78                       |
| 7   | 108         | 1800   | 105.6                    | 89                       |
| 8   | 105         | 1500   | 105.8                    | 56                       |
| 9   | 110         | 1400   | 107.2                    | 77                       |

---

## 2. Feature Vectors for T=5 to T=9

Format: `[Close_t, Volume_t, SMA_t, RSI_t]`

- **T=5:**
- **T=6:**
- **T=7:**
- **T=8:**
- **T=9:**

---

## 3. State Space Matrices for T=6 to T=9 (window size = 2)

- **T=6:**

- **T=7:**

- **T=8:**

- **T=9:**

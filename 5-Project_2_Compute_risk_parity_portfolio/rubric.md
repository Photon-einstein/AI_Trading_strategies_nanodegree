# Rubric

> Use this project rubric to understand and assess the project criteria.

---

## 1. Data Collection and Preprocessing

| Criteria | Submission Requirements |
|----------|------------------------|
| The student will be able to retrieve and preprocess financial time-series data for further analysis. | The code demonstrates the use of a Python library to retrieve financial time-series data for the desired assets and transforms it to obtain the desired variables. |
| The student will be able to reduce noise in financial time-series data using a resampling technique. | The code applies a monthly resampling technique to the data to improve the signal-to-noise ratio, producing a dataset with the desired frequency. |

---

## 2. Risk Parity Weight Computation and Portfolio Returns Calculation

| Criteria | Submission Requirements |
|----------|------------------------|
| The student will be able to compute risk parity weights for a portfolio. | The code uses a rolling window approach to compute and shift risk parity weights by one period for a given portfolio. |
| The student will be able to calculate portfolio returns. | The code calculates returns for a risk parity portfolio using the computed weights. |

---

## 3. Performance Evaluation and Visualization

| Criteria | Submission Requirements |
|----------|------------------------|
| The student will be able to evaluate the performance of a portfolio using various performance metrics. | The code demonstrates the ability to evaluate the performance of a portfolio using various performance metrics, such as the annualized mean return, annualized volatility, skewness, kurtosis, maximum drawdown, Sharpe ratio, Sortino ratio, and Calmar ratio. The resulting performance metrics are interpreted and used to make investment decisions. |
| The student will be able to visualize the performance of a portfolio using appropriate plots. | The code demonstrates the ability to visualize the performance of a portfolio using appropriate plots, such as a plot of the cumulative returns of the portfolio and a plot of the drawdowns of the portfolio. The resulting plots are interpreted and used to make investment decisions. |
| The student will be able to apply the performance evaluation and visualization to a real-world dataset. | The code demonstrates the ability to apply the performance evaluation and visualization to a real-world dataset of front-month futures data for the S&P 500, 10-year Treasuries, gold, and the US dollar. The resulting performance metrics and plots are interpreted and used to make investment decisions. |

---

## Suggestions to Make Your Project Stand Out

- **Incorporate additional data sources:** Consider including data on individual stocks, commodities, or other asset classes beyond the front-month futures data for the S&P 500, 10-year Treasuries, gold, and the US dollar. This would allow for a more diverse and potentially more robust portfolio.

- **Visualize portfolio composition:** In addition to visualizing performance, consider visualizing the composition of the portfolio over time using a stacked area chart or similar visualization. This would provide a better understanding of how the portfolio's assets are weighted and how those weights change over time.

- **Include a detailed report:** Consider including a detailed report that summarizes the project and provides additional insights into the methodology and results. This report could include sections on:
  - Data collection and preprocessing
  - Risk parity weight computation and portfolio returns calculation
  - Performance evaluation and visualization
  - A conclusion summarizing key findings and potential areas for future work

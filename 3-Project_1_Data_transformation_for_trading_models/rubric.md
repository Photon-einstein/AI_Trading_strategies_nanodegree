# Rubric

> Use this project rubric to understand and assess the project criteria.

---

## 1. Load Data

| Criteria                                        | Submission Requirements                                                       |
| ----------------------------------------------- | ----------------------------------------------------------------------------- |
| Download data from GitHub into Pandas dataframe | Student will create a Pandas dataframe that has the CSV imported from GitHub. |

---

## 2. Data Preprocessing

| Criteria                                                  | Submission Requirements                                                                                                                                                     |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Check for missing data                                    | Student will run appropriate functions on the DataFrame containing the data and report the number missing per column/attribute.                                             |
| Forward fill missing data                                 | Student will use the information from the prior step (checking for missing data) to fill in any missing data in columns that require it. They should be using forward fill. |
| Remove special characters and convert to numeric/datetime | The student will fill in the `convert_dollar_columns_to_numeric` function using code that replaces dollar signs with empty strings (`''`).                                  |
| Align datetime data                                       | The student will change the datetime attribute for the inflation DataFrame so that it falls on the last day of the month.                                                   |
| Upsample, downsample and interpolate data                 | There are two separate steps here. The first creates quarterly average data and the second interpolates weekly data from monthly data.                                      |

---

## 3. Industry Best Practices

| Criteria                        | Submission Requirements                                                                                                                                                                                                                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Normalize/standardize a feature | Students will create a new attribute that holds the standardized GDP values. The solution does this manually by calculating the min and max and using it in the formula. However, it's also acceptable if students use the `StandardScaler` method from sklearn or some other similar method. |

---

## 4. EDA

| Criteria                                                                                                              | Submission Requirements                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Plotting a time series of adjusted open vs close price                                                                | The student will plot a line chart that displays the open and close price for Apple stock for the last three months.                                                                                                            |
| Plotting a histogram of a stock's closing price in the last three months                                              | The student will again use the last 3 months of data to plot a histogram of Apple closing price.                                                                                                                                |
| Calculating correlation between a stock price and a macroeconomic variable and plotting the output as a heatmap       | The student will plot a heatmap of correlations between Microsoft and Apple returns and inflation. Note that this will be a 3x3 heatmap matrix as it will include the pairwise correlations of Apple, Microsoft, and inflation. |
| Calculating rolling volatility (standard deviation) of a stock's price for last 3 months and plotting as a line chart | The student will calculate the rolling standard deviation for Apple stock. They will then plot the rolling SD and the Apple closing price on the same chart, but using two y-axes.                                              |

---

## 5. Export Data

| Criteria                                                             | Submission Requirements                                                                                                                                                                   |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Export transformed data as a CSV back to local computing environment | The student will create an output CSV of the transformed data. Depending on whether they merged DataFrames in the prior steps, they may be outputting one or more CSV files in this step. |

---

## Suggestions to Make Your Project Stand Out

- Original graphs that include interesting or unique insights using the available data (e.g., using a transformation on a data series instead of plotting the raw data).
- Plotting multiple time series on the same graph using two y-axis labels.
- For the EDA portion, make charts stand out by adding formatting such as titles, legends (where appropriate), and changing the default color scheme.

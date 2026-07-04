Data Handling
Criteria Submission Requirements
The student will be able to load data to an SQLite database from a CSV file

The tables prices and positions are created in the database
The prices table is correctly populated by the data from the SP500.csv
The GBM Model
Criteria Submission Requirements
The student will be able to calibrate a GBM model to a price series

Correct log-transform of the historical prices
Correct estimation of the 1st and the 2nd moments of the price series using bootstrap
Correct calculation of the mu and the sigma parameters from the first two moments of the bootstrap sample.
The student will be able to forecast the price at a future time.

Correct calculation of the predicted price and its confidence interval.

Computation of the Expected Shortfall
Criteria Submission Requirements
The student will be able to calculate the expected shortfall.

The formula of the expected shortfall is coded correctly in the GBM.expected_shortfall function.

Suggestions to Make Your Project Stand Out
Consider using the Student’s t test to check the significance of an observed momentum. At what level of significance will you act on it?
Find out the days on which your strategy performs the best and the worst, respectively. What happened on these days?
Calculate the mean and the standard deviation of your daily returns. Then calculate the Sharpe ratio of your strategy in the test period. How does it compare to the return of a savings account?

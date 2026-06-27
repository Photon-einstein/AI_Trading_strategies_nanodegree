from scipy.stats import norm, shapiro

X = norm.rvs(size=100)
print(shapiro(X))

# AI Trading Strategies Nanodegree

## About

The AI Trading Strategies Nanodegree equips learners with the skills to build and optimize AI-based trading models. The program covers key areas like ideation, data preprocessing, model development, backtesting, and optimization. Graduates will differentiate AI trading models, select the right model for specific applications, ingest and prepare data, and backtest models using industry best practices. Additionally, learners will master model optimization and detect model drift to ensure ongoing performance.

- **Level:** Advanced
- **Projects:** 5
- **Courses:** 8
- **Lessons:** 34

## Program Outline

1. Welcome to the Nanodegree Program
2. Building a Workflow for AI
3. Preparing for Data Analysis
4. Evaluating Returns and Backtesting
5. (more courses to be added as the program progresses)

## Skills

- Automated Plan Optimization
- Backtesting
- Feature Engineering
- Financial Analysis With AI
- Quant Workflow
- Unsupervised Machine Learning
- Model Drift
- Hyperparameter Tuning

## To activate the environment

```bash
python3 -m venv .venv
source .venv/bin/activate
deactivate
```

## To get the requirements and install from it

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

## Conda commands

```bash
conda create -n ai_trading python=3
conda activate ai_trading
conda list
conda env list
conda install numpy pandas matplotlib scikit-learn

conda update --all
conda upgrade --all
conda env export > environment.yaml
conda env create -f environment.yaml
conda env remove -n env_name

conda deactivate
```

[Conda Command reference guide](https://docs.conda.io/projects/conda/en/latest/commands/index.html)

## To start Jupyter notebook

```bash
jupyter notebook
```

[Jupyter documentation](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/examples_index.html)

## Useful libraries

### Numpy

[Numpy official user guide](https://numpy.org/doc/stable/user/index.html)

### Pandas

[Pandas official user guide](https://pandas.pydata.org/pandas-docs/stable/)

### Matplotlib

[Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)

### Scikit-learn

[Scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)

## Projects

### Project 1 — ML Pipeline for Feature Engineering

**Folder:** [3-Project_1_Data_transformation_for_trading_models/](3-Project_1_Data_transformation_for_trading_models/)

Built a complete data engineering pipeline using macroeconomic indicators (GDP, inflation) and historical stock prices (Apple, Microsoft). Key tasks included:

- Ingesting data from remote CSV sources into Pandas DataFrames
- Cleaning data: handling missing values with forward-fill, removing special characters, converting columns to numeric and datetime types
- Resampling: upsampling monthly data to weekly (interpolation) and downsampling to quarterly averages
- Normalizing GDP values using min-max standardization
- Exploratory Data Analysis (EDA): time-series plots, histograms, correlation heatmaps, and rolling volatility charts with dual y-axes
- Exporting transformed datasets back to CSV

**Key libraries:** `pandas`, `matplotlib`, `seaborn`

---

### Project 2 — Risk Parity Portfolio

**Folder:** [5-Project_2_Compute_risk_parity_portfolio/](5-Project_2_Compute_risk_parity_portfolio/)

Constructed and evaluated a risk parity portfolio using front-month futures data for the S&P 500, 10-year Treasuries, gold, and the US dollar. Key tasks included:

- Retrieving and preprocessing financial time-series data, applying monthly resampling to reduce noise
- Computing risk parity weights using a rolling window approach, shifted by one period to avoid look-ahead bias
- Calculating portfolio returns from the computed weights
- Evaluating portfolio performance with metrics: annualized mean return, annualized volatility, skewness, kurtosis, maximum drawdown, Sharpe ratio, Sortino ratio, and Calmar ratio
- Visualizing cumulative returns and drawdown periods

**Key libraries:** `pandas`, `numpy`, `matplotlib`

---

### Project 3 — Reinforcement Learning Trading Agent

**Folder:** [8-Project_3_Reinforcement_learning_Trading_agent/](8-Project_3_Reinforcement_learning_Trading_agent/)

Built a Deep Q-Network (DQN) agent from scratch to trade Google stock (GOOG) using Keras. Key tasks included:

- Cleaning and preparing financial tick data, computing 20-day Bollinger Bands as state features
- Normalizing features with `StandardScaler` and splitting data into training/test sets
- Designing a custom DQN architecture (Keras) with an ε-greedy exploration-exploitation policy
- Implementing experience replay with mini-batches and Q-value updates via the Bellman equation
- Writing the training loop: state transitions, reward shaping for buy/sell actions, and memory updates
- Testing the trained agent by loading a saved Keras checkpoint

**Key libraries:** `keras`, `numpy`, `sklearn`, `pandas`

---

### Project 4 — Optimizing AI Trading Algorithms

**Folder:** [10-Project_4_Optimizing_trading_algorithms/](10-Project_4_Optimizing_trading_algorithms/)

Optimized a binary classification model to predict the direction of 5-day XLV (Healthcare Sector ETF) price movements using market uncertainty signals. Key tasks included:

- Acquiring and aligning daily XLV price data, VIX (volatility index), and Google Trends data for the search term "recession"
- Feature engineering: RSI, Bollinger Bands, and trend-based features
- Addressing overfitting/underfitting and performing hyperparameter tuning with `GridSearchCV`
- Evaluating a `RandomForestClassifier` using accuracy, precision, recall, F1-score, and confusion matrix
- Applying feature selection techniques and analyzing learning curves

**Key libraries:** `sklearn`, `yfinance`, `ta`, `pandas`, `plotly`, `seaborn`

---

### Project 5 — Momentum-Based Trading

**Folder:** [12-Project_5_Momentum_based_trading/](12-Project_5_Momentum_based_trading/)

Implemented a momentum-based trading strategy on S&P 500 data using stochastic modeling and risk metrics. Key tasks included:

- Loading S&P 500 price data into an SQLite database (`prices` and `positions` tables)
- Calibrating a Geometric Brownian Motion (GBM) model: log-transforming prices, bootstrapping the first two moments, and estimating drift (μ) and volatility (σ)
- Forecasting future prices with confidence intervals using the calibrated GBM
- Computing the Expected Shortfall (ES) as a tail-risk measure
- Backtesting the momentum strategy and analyzing best/worst-performing days

**Key libraries:** `sqlite3`, `numpy`, `pandas`, `scipy`, `matplotlib`

---

## Certificate of completion

[Certificate of graduation](www.udacity.com/certificate/e/fb8d15d2-85bc-11f0-aab2-eb32a0c4c27d)

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

# Project Rubric

Use this rubric to understand and assess the project criteria.

---

## 1. Data Preparation

### Clean financial tick data in preparation for training

- Load data, view data, fill missing values, and plot filled data.

### Training feature / state representation selection

- Filter the OHLC data down to just `Close`.
- Use `Close` to calculate 20-day Bollinger Bands (upper and lower bands).

### Normalize data for input into a neural network

- Normalize each training feature using `sklearn` `StandardScaler` (centers data to zero mean with unit variance).

### Split dataset into training and test sets

- Split the dataset in half: first half for training, second half for test.
- Display both datasets to verify there is no overlap.
- Convert DataFrames to NumPy arrays (required for Keras).

---

## 2. Agent Definition

### Write a custom DQN architecture in Keras

- Build a DQN from scratch using Keras.
- Layer sizes, model type, optimizer type, and learning rate are provided.

### Define the action policy for a DQN agent

- Implement an ε-greedy exploration-exploitation policy.
- Use Q-values from the model to select the best action during exploitation.

### Define the experience replay (i.e. DQN fitting) process

- Define a mini-batch of recent memory entries.
- Update target Q-values using the Bellman equation.
- Fit the DQN model on the updated target Q-values.

### Define an RL Agent

- All of the above methods must be encapsulated in a custom `Agent` class.

---

## 3. Training and Testing

### Get the current state of the environment

- Implement a `get_state` helper function.
- Must return a 2-day state representation: today's `Close` and Bollinger Bands + yesterday's `Close` and Bollinger Bands.

### Implement & run the training loop

- Complete the training skeleton with:
  - Getting the current and next state.
  - Performing inverse transforms with the normalizers to recover true price data.
  - Defining rewards for buy and sell actions.
  - Updating the agent memory after each step.
  - Running experience replay for every mini-batch of memory.

### Implement & run the testing loop

- Complete the test loop skeleton.
- Load the trained model from a saved Keras checkpoint by setting the agent to test mode.

# Stochastic and Deterministic Policy Determination

This problem is designed to help you understand the difference between stochastic and deterministic strategies.

## Scenario Definition

Below we have defined four example trading policies.

## Objective

Identify which policies are stochastic, and which are deterministic.

---

### Policy A

```python
def trading_policy_A(current_price, ma):

    [score_buy, score_sell, score_hold] = ActionScoreNet(state=[current_price, ma])

    action_idx = argmax([score_buy, score_sell, score_hold])

    if action_idx == 0:
        return “BUY”

    elif action_idx == 1:
        return “SELL”

    else:
        return “HOLD”
```

- Deterministic policy

### Policy B

```python
def trading_policy_B(current_price, ma):

    [score_buy, score_sell, score_hold] = ActionScoreNet(state=[current_price, ma])

    action = random.choices([“BUY”, “SELL”, “HOLD”], weights=[score_buy, score_sell, score_hold], k=1)

    return action
```

- Stochastic policy

### Policy C

```python
def trading_policy_C(current_price, ma):

    if current_price < 0.3*ma:
        return “BUY”

    elif current_price > 0.7*ma:
        return “SELL”

    else:
        return “HOLD”
```

- Deterministic policy

### Policy D

```python
def trading_policy_D(current_price, ma, e):

    if random.random() <= e:
        [score_buy, score_sell, score_hold] = ActionScoreNet(state=[current_price, ma])

        action_idx = argmax([score_buy, score_sell, score_hold])

        if action_idx == 0:
            return “BUY”

        elif action_idx == 1:
            return “SELL”

        else:
            return “HOLD”

    else:
        return random.choice([“BUY”, “SELL”, “HOLD”])
```

- Stochastic policy

## Answers

**Stochastic:** B, D

**Deterministic:** A, C

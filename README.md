# Black–Scholes Option Pricing Engine

This project implements a clean, from-scratch Black–Scholes pricing engine for
European call options. It includes option pricing, implied volatility
calculation, and the most important Greek (delta).

The focus of this project is clarity of intuition and correctness of
implementation, rather than treating formulas as black boxes.

---

## Features

- Black–Scholes call option pricing
- Implied volatility solver using binary search
- Call option delta (Greek)
- Clean, modular Python package structure
- Example using NIFTY-like inputs

---

## Project Structure

black-scholes-engine/
├── src/
│   └── bs_engine/
│       ├── bs.py
│       ├── implied_vol.py
│       ├── greeks.py
│       └── utils.py
├── examples/
│   └── nifty_example.py
├── requirements.txt
├── .gitignore
└── README.md

---

## High-Level Idea

A European call option payoff at expiry is:

max(S_T - K, 0)

When the option is in-the-money, the payoff can be viewed as:
- receiving the underlying price S_T
- paying the strike price K

The Black–Scholes model prices the option by:
- weighting future outcomes by probability
- separating price contribution and strike cost
- expressing uncertainty using the normal distribution

This leads to the closed-form solution:

Call Price = S · N(d1) − K · e^(−rT) · N(d2)

This project implements this logic step by step in code.

---

## Running the Project (Windows)

Step 1: Create and activate virtual environment

python -m venv venv  
venv\Scripts\activate  

Step 2: Install dependencies

pip install -r requirements.txt  

Step 3: Run example

set PYTHONPATH=src  
python examples\nifty_example.py  

Example output:

Call option price: 196.26  
Recovered implied vol: 0.2000  
Call delta: 0.32  

---

## What This Project Demonstrates

- Understanding of option payoff structure
- Practical implementation of Black–Scholes pricing
- Implied volatility inversion from market prices
- Clean, maintainable Python code
- Ability to connect financial intuition with software design

---

## Possible Extensions

- Put option pricing and put–call parity
- Additional Greeks (gamma, theta, vega)
- Integration with live NSE option chain data
- Volatility smile or surface construction

# Black–Scholes & Black-76 Option Pricing Engine

This project implements a clean, from-scratch option pricing engine for
European options, covering both **Black–Scholes (spot-based)** and
**Black-76 (futures-based)** models.

It includes option pricing, implied volatility calculation, and key Greeks.
The focus of this project is clarity of intuition and correctness of
implementation, rather than treating formulas as black boxes.

This repository is designed to reflect how options are **actually priced and
hedged in practice**, especially for **Indian index options (NIFTY)**.

---

## Features

- Black–Scholes call option pricing (spot-based)
- Black-76 call option pricing (futures-based, index-compatible)
- Implied volatility solvers (Black–Scholes and Black-76)
- Option Greeks: Delta, Gamma, Theta
- Integration with live NSE option chain data (with safe fallback)
- Clean, modular Python package structure
- Realistic examples using NIFTY options

---

## Project Structure

    black-scholes-engine/
    ├── src/
    │   └── bs_engine/
    │       ├── black_scholes.py      # Spot-based Black–Scholes
    │       ├── black_76.py            # Futures-based Black-76
    │       ├── implied_vol.py
    │       ├── greeks.py
    │       ├── nse_data.py
    │       └── utils.py
    ├── examples/
    │   ├── nifty_example.py
    │   ├── nifty_example_real.py
    │   ├── nifty_black76_example.py
    │   └── nifty_black76_real.py
    ├── data/
    │   └── nifty_sample.json
    ├── requirements.txt
    ├── .gitignore
    └── README.md

---

## High-Level Idea

A European call option payoff at expiry is:

    max(S_T − K, 0)

When the option finishes in-the-money, the payoff can be viewed as:
- receiving the underlying price
- paying the strike price

Option pricing answers one core question:

> What is the fair price today for a payoff that is uncertain in the future?

The key idea behind both Black–Scholes and Black-76 is:
- uncertainty can be removed by hedging
- a hedged (risk-free) portfolio must grow at the risk-free rate
- this constraint uniquely determines the option price

---

## Models Implemented

### Black–Scholes (Spot-Based)

Used when:
- the underlying asset itself is tradable (e.g., equities)

Formula:

    Call Price = S · N(d1) − K · e^(−rT) · N(d2)

---

### Black-76 (Futures-Based)

Used when:
- options are written on **futures contracts**
- hedging is done using futures
- this is the correct model for **Indian index options (NIFTY, BANKNIFTY)**

Formula:

    Call Price = e^(−rT) · [ F · N(d1) − K · N(d2) ]

This project explicitly implements Black-76 to reflect **real Indian market
structure**, rather than applying Black–Scholes blindly.

---

## NSE Data Integration

The project integrates with live NSE option-chain data.

Due to NSE blocking unauthenticated futures requests:
- **spot price is used as a proxy for futures price**
- this approximation is reasonable for short-dated index options
- the code structure cleanly supports real futures prices if available

This design choice is explicit and documented, not hidden.

---

## Running the Project (Windows)

### Step 1: Create and activate virtual environment

    python -m venv venv
    venv\Scripts\activate

### Step 2: Install dependencies

    pip install -r requirements.txt

### Step 3: Run examples

Set PYTHONPATH:

    set PYTHONPATH=src

Run Black–Scholes example:

    python examples\nifty_example.py

Run Black-76 example (real data):

    python examples\nifty_black76_real.py

---

## Example Output

    NIFTY Spot: 25966.4
    NIFTY Futures: 25966.4

    Strike 26000 | Market Price 165
      IV: 0.116
      Delta: 0.500
      Gamma: 0.000954
      Theta: -14.022

---

## What This Project Demonstrates

- Deep understanding of option payoff mechanics
- Correct distinction between spot-based and futures-based options
- Practical application of risk-neutral pricing
- Implied volatility inversion from market prices
- Implementation of Greeks consistent with market structure
- Clean, extensible Python engineering
- Ability to connect financial theory with real-world data

---

## Possible Extensions

- Put options and put–call parity
- Volatility smile and surface construction
- Monte Carlo option pricing
- Term-structure of interest rates
- Support for additional indices and expiries

---

## Disclaimer

This project is for **educational and research purposes only**.
It is not intended for live trading or financial advice.

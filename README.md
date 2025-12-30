# Black–Scholes & Black-76 Option Pricing Engine

This project implements a clean, from-scratch option pricing engine for
European options, covering both **Black–Scholes (spot-based)** and
**Black-76 (futures-based)** models.

It includes option pricing, implied volatility calculation, key Greeks, and
real-world analysis of **volatility skew** using live **NIFTY index option
data**.

The focus of this project is clarity of intuition, correctness of
implementation, and alignment with **how index options are actually priced
and hedged in practice**, rather than treating formulas as black boxes.

---

## Features

- Black–Scholes call option pricing (spot-based)
- Black-76 call option pricing (futures-based, index-compatible)
- Implied volatility solvers (Black–Scholes and Black-76)
- Option Greeks: Delta, Gamma, Theta
- Integration with live NSE option chain data (with safe fallback)
- Volatility skew analysis using real NIFTY options
- CSV export and visualization of implied volatility skew
- Clean, modular Python package structure
- Realistic examples using Indian index options

---

## Project Structure

```
black-scholes-engine/
├── src/
│   └── bs_engine/
│       ├── black_scholes.py
│       ├── black_76.py
│       ├── implied_vol.py
│       ├── greeks.py
│       ├── nse_data.py
│       └── utils.py
├── examples/
│   ├── nifty_example.py
│   ├── nifty_example_real.py
│   ├── nifty_black76_example.py
│   ├── nifty_black76_real.py
│   ├── volatility_skew_bs.py
│   └── volatility_skew_black76.py
├── data/
│   ├── nifty_sample.json
│   └── derived/
│       └── nifty_volatility_skew_black76.csv
├── Figure 1.png
├── requirements.txt
├── .gitignore
└── README.md
```

---

## High-Level Idea

A European call option payoff at expiry is:

```
max(S_T − K, 0)
```

When the option finishes in-the-money, the payoff can be viewed as:
- receiving the underlying price
- paying the strike price

Option pricing answers one core question:

> What is the fair price today for a payoff that is uncertain in the future?

Both Black–Scholes and Black-76 rely on the same principle:
- uncertainty can be eliminated through continuous hedging
- a hedged portfolio becomes risk-free
- a risk-free portfolio must grow at the risk-free rate
- this condition uniquely determines the option price

---

## Models Implemented

### Black–Scholes (Spot-Based)

Used when:
- the underlying asset itself is tradable (e.g., equities)

Formula:

```
Call Price = S · N(d1) − K · e^(−rT) · N(d2)
```

---

### Black-76 (Futures-Based)

Used when:
- options are written on **futures contracts**
- hedging is done using futures
- this is the correct model for **Indian index options (NIFTY, BANKNIFTY)**

Formula:

```
Call Price = e^(−rT) · [ F · N(d1) − K · N(d2) ]
```

This project explicitly implements Black-76 to reflect **real Indian market
structure**, rather than applying Black–Scholes blindly.

---

## NSE Data Integration

The project integrates with live NSE option-chain data.

Due to NSE blocking unauthenticated futures requests:
- **spot price is used as a proxy for futures price**
- this approximation is reasonable for short-dated index options
- the code structure cleanly supports real futures prices if available

This design choice is explicit and documented.

---

## Volatility Smile vs Volatility Skew

A common expectation when learning option pricing is that implied volatility
forms a symmetric **volatility smile** around the at-the-money (ATM) strike.

However, analysis of **real NIFTY option data** reveals a clear
**volatility skew**, not a smile.

Observed behavior:
- Higher implied volatility for lower strikes (downside protection)
- Gradual decline in implied volatility as strike increases
- Asymmetry around ATM
- Persistent downside skew

This reflects real market behavior where:
- downside risk is priced more aggressively
- crash protection demand dominates
- index options are structurally asymmetric instruments

The volatility skew extracted using Black-76 is visualized below.

![Volatility Skew (Black-76)](Figure%201.png)

---

## Running the Project (Windows)

### Step 1: Create and activate virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Run examples

Set PYTHONPATH:

```
set PYTHONPATH=src
```

Run Black–Scholes example:

```
python examples\nifty_example.py
```

Run Black-76 example with real data:

```
python examples\nifty_black76_real.py
```

Run volatility skew analysis:

```
python examples\volatility_skew_black76.py
```

---

## Example Output

```
Strike | Market Price | Black-76 IV
26000  | 165.00       | 0.2444
26100  | 113.00       | 0.2371
26200  | 73.50        | 0.2299
...
```

CSV output is generated at:

```
data/derived/nifty_volatility_skew_black76.csv
```

---

## What This Project Demonstrates

- Deep understanding of option payoff mechanics
- Correct distinction between spot-based and futures-based options
- Practical application of risk-neutral pricing
- Implied volatility inversion from market prices
- Real-world volatility skew analysis
- Market-structure-aware modeling for Indian indices
- Clean, extensible Python engineering
- Ability to connect financial theory with live market data

---

## Possible Extensions

- Volatility surface construction (strike × maturity)
- Monte Carlo option pricing
- Term-structure of interest rates
- Support for multiple expiries and indices
- Risk metrics and scenario analysis

---

## Disclaimer

This project is for **educational and research purposes only**.
It is not intended for live trading or financial advice.

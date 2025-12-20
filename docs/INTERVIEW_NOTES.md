# Interview Notes — Black–Scholes Option Pricing Project

This document contains my own notes on how to explain this project
clearly during interviews. The goal is to focus on intuition,
design decisions, and trade-offs rather than formulas.

---

## 1. How I introduce this project (30 seconds)

I built a Black–Scholes option pricing engine from scratch.
The project prices European call options, computes implied volatility
from market prices, and exposes core Greeks like delta.

The main goal was to understand the intuition behind option pricing
and implement it cleanly, rather than using the formula as a black box.

---

## 2. What problem does Black–Scholes solve?

At expiry, a call option payoff depends on two things:
1. Whether the final price crosses the strike
2. How high the price goes if it does

Black–Scholes answers a simple question:
"What is the fair price of this uncertain payoff today?"

It does this by taking an expected value of future outcomes
under uncertainty and discounting it back to the present.

---

## 3. How I explain the model without formulas

I explain it in three steps:

1. First, decide which future outcomes matter  
   Only outcomes where the final price is above the strike
   contribute to the payoff.

2. Second, measure how strongly those outcomes contribute  
   Higher prices contribute more than lower ones.

3. Third, translate future uncertainty into today’s price  
   This is done using probability weights and discounting.

The final formula is just a compact way of expressing this logic.

---

## 4. What is implied volatility (very important)

Implied volatility is not a forecast.

It is the volatility value that makes the Black–Scholes price
equal to the market price of the option.

In other words:
The market gives us the price, and we invert the model
to extract the uncertainty implied by that price.

In this project, I compute implied volatility using binary search,
because the option price increases monotonically with volatility.

---

## 5. What does delta represent?

Delta measures how sensitive the option price is
to changes in the underlying price.

In Black–Scholes, call delta is N(d1).

Intuitively:
- Deep ITM options have delta close to 1 and behave like futures
- Far OTM options have delta close to 0
- Near ATM options have delta around 0.5

Delta can be interpreted as probability-weighted exposure
to the underlying price.

---

## 6. Why the project is structured this way

I separated the code into modules with clear responsibilities:

- bs.py: pricing logic
- implied_vol.py: volatility inversion
- greeks.py: risk sensitivities
- utils.py: mathematical utilities

This keeps the code easy to extend, test, and reason about.
The project is structured as a proper Python package
rather than a single script.

---

## 7. What this project demonstrates about me

This project demonstrates that I can:
- reason about financial models at an intuitive level
- translate math into clean, working code
- think carefully about design and structure
- validate logic through end-to-end examples

---

## 8. How I would extend this project

Possible next steps include:
- adding more Greeks (gamma, theta)
- integrating live option-chain data
- building a small backtesting or analytics layer

I intentionally kept the core project focused and correct
rather than overloading it with features.

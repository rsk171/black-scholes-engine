import sys
import os

from bs_engine.bs import call_price
from bs_engine.implied_vol import implied_vol_call
from bs_engine.greeks import call_delta

S = 26000
K = 26400
T = 10/365
r = 0.06
true_sigma = 0.20

# Step 1: price option using known volatility
price = call_price(S, K, T, r, true_sigma)
print("Call option price:", round(price, 2))

# Step 2: recover volatility from that price
iv = implied_vol_call(price, S, K, T, r)
print("Recovered implied vol:", round(iv, 4))

delta = call_delta(S, K, T, r, true_sigma)
print("Call delta:", round(delta, 4))

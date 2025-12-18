import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from bs import call_price

S = 26000
K = 26400
T = 10/365
r = 0.06
sigma = 0.20

price = call_price(S, K, T, r, sigma)

print("Call option price:", round(price, 2))

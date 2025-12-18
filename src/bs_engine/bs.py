import math
from bs_engine.utils import normal_cdf

def d1(S, K, T, r, sigma):
    return (math.log(S/K) + (r + 0.5*sigma**2) * T)/(sigma * math.sqrt(T))

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * math.sqrt(T)

def call_price(S, K, T, r, sigma):
    """
    Black-Scholes call option price
    """
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)

    return S * normal_cdf(D1) - K * math.exp(-r * T) * normal_cdf(D2)

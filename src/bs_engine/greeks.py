from bs_engine.bs import d1
from bs_engine.utils import normal_cdf

def call_delta(S, K, T, r, sigma):
    """
    Black-Scholes delta for a call option
    """
    return normal_cdf(d1(S, K, T, r, sigma))
